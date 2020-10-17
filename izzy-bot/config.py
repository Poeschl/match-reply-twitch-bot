import os
from os import path

from yaml import SafeLoader, dump, load

DEBUG = 'debug'
IRC_TOKEN = 'irc_token'
CLIENT_ID = 'client_id'
BOT_NAME = 'bot_name'
BOT_PREFIX = 'bot_prefix'
TARGET_CHANNEL = 'target_channel'
TARGET_BOT = 'target_bot'

DEFAULT_CONFIG_FOLDER = 'config'


class Config:
    config_data = {
        DEBUG: False,
        IRC_TOKEN: 'oauth:',
        CLIENT_ID: '',
        BOT_NAME: '',
        BOT_PREFIX: '!',
        TARGET_CHANNEL: '',
        TARGET_BOT: 'myBot'
    }

    def __init__(self):
        config_folder = os.getenv('CONFIG_FILE', DEFAULT_CONFIG_FOLDER)
        if not path.exists(config_folder):
            os.mkdir(config_folder)
        self.config_file = config_folder + '/config.yaml'
        self._parse_config()

    def _parse_config(self):
        if path.exists(self.config_file):
            with open(self.config_file, 'r+') as file:
                stored_config_data = load(file, SafeLoader)
                self.config_data = {**self.config_data, **stored_config_data}
                file.seek(0)
                dump(self.config_data, file)
                file.truncate()
        else:
            with open(self.config_file, 'w') as file:
                dump(self.config_data, file)

    def get_config(self, key: str):
        return self.config_data[key]

    @staticmethod
    def get_config_folder():
        return os.getenv('CONFIG_FILE', DEFAULT_CONFIG_FOLDER)
