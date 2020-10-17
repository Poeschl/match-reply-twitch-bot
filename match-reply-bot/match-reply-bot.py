import logging

import sys
from regex import regex
from twitchio.ext import commands

from config import Config, IRC_TOKEN, CLIENT_ID, BOT_NAME, BOT_PREFIX, TARGET_CHANNEL, TARGET_USER, RULES


class MatchReplyBot(commands.Bot):

    def __init__(self, config):
        super().__init__(
            irc_token=config.get_config(IRC_TOKEN),
            client_id=config.get_config(CLIENT_ID),
            nick=config.get_config(BOT_NAME),
            prefix=config.get_config(BOT_PREFIX),
            initial_channels=[config.get_config(TARGET_CHANNEL)]
        )
        self.target_user = config.get_config(TARGET_USER)
        self.rules = config.get_config(RULES)
        self.active = True

    async def event_ready(self):
        print("Online....")

    async def event_message(self, ctx):
        if ctx.author.name.lower() == self.nick.lower():
            # Commands only the the bot user
            await self.handle_commands(ctx)

        if self.active and ctx.author.name.lower() == self.target_user.lower():
            # reply logic only for the targeted user
            for rule in self.rules:
                if regex.search(rule.get('pattern'), ctx.content):
                    await ctx.channel.send(rule.get('reply'))

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

    bot = MatchReplyBot(config)
    bot.run()


if __name__ == '__main__':
    main()
