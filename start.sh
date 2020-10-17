#!/usr/bin/env bash
set -e

python3.8 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

PYTHONPATH="$(printf "%s:" izzy-bot/)"
export PYTHONPATH=$PYTHONPATH PYTHONUNBUFFERED=1
python3 -u izzy-bot/izzy-bot.py
