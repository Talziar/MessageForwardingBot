"""Telegram Bot."""

import logging

from pyrogram import Client

from message_forwarding_bot import API_HASH, API_KEY, USERNAME
from message_forwarding_bot.modules import ALL_MODULES
from message_forwarding_bot.utils.loader import load_modules

LOGGER = logging.getLogger(__name__)
BOT = Client(USERNAME, API_KEY, API_HASH)
BOT_INFO = {}
BOT.parse_mode = "markdown"

LOGGER.info("Bot started!")

load_modules(ALL_MODULES, __package__)
BOT.run()
