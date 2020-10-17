# Match Reply Twitch Bot

This is a simple bot, which scans the chat of a specified channel for patterns and reply the given text.

## Config

The configuration ist done in the `config.yaml` file. It will get generated on the first start.

### `bot_name`
The name under which the bot is posting his texts.

### `bot_prefix`
The prefix for the bot commands. Defaults to `!`

### `client_id`
The client id of twitch.
To receive it, [register your app with Twitch dev](https://dev.twitch.tv/console/apps/create) and get the `client_id` from there.

### `irc_token`
The oauth token to access Twitch.
[Request the token](https://twitchapps.com/tmi/) on Twitch, it starts with `oauth:`.

### `target_user`
The user to listen for.

### `target_channel`
The Twitch channel for the chat to listen to.

### `rules`
The rules to search and reply. They are defined as pairs of `pattern` and `reply`. The pattern accepts also regex.
For example:
```yaml
rules:
  - pattern: 'Ping'
    reply: 'Pong'
```

## Commands

### `!botstart`

Starts the farming logic

### `!botstop`

Stops the farming
