import logging

import sys
from twitchio.ext import commands

from config import Config, IRC_TOKEN, CLIENT_ID, BOT_NAME, BOT_PREFIX, TARGET_CHANNEL, TARGET_BOT


class IzzyBot(commands.Bot):

    def __init__(self, config):
        super().__init__(
            irc_token=config.get_config(IRC_TOKEN),
            client_id=config.get_config(CLIENT_ID),
            nick=config.get_config(BOT_NAME),
            prefix=config.get_config(BOT_PREFIX),
            initial_channels=[config.get_config(TARGET_CHANNEL)]
        )
        self.target_bot = config.get_config(TARGET_BOT)
        self.active = False

    async def event_ready(self):
        print("Online....")

    async def event_message(self, ctx):
        if ctx.author.name.lower() == self.nick.lower():
            # Commands only the the bot user
            await self.handle_commands(ctx)

        if self.active and ctx.author.name.lower() == self.target_bot.lower():
            # logic only for the targeted bot
            if 'Gegner wieder verteilt'.lower() in ctx.content.lower():
                await ctx.channel.send("!boss <Jarvis>")

    @commands.command(name='botstart')
    async def bot_start(self, ctx):
        await ctx.send(f'Starting bot...')
        self.active = True

    @commands.command(name='botstop')
    async def bot_stop(self, ctx):
        await ctx.send(f'Stopping bot...')
        self.active = False


def main():
    logging.basicConfig(level=logging.INFO)
    error_handler = logging.root.handlers[0]
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(error_handler.formatter)
    logging.root.removeHandler(error_handler)
    logging.root.addHandler(log_handler)

    config = Config()

    bot = IzzyBot(config)
    bot.run()


if __name__ == '__main__':
    main()
