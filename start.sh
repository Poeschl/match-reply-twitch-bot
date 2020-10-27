#!/usr/bin/env bash
set -e

python3.8 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

export PYTHONUNBUFFERED=1
exec python3 -u match-reply-bot/match-reply-bot.py
