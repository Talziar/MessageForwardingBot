"""Telegram Bot."""

import asyncio
import logging

from pyrogram import Client, idle

from message_forwarding_bot import API_HASH, API_KEY, USERNAME
from message_forwarding_bot.modules import ALL_MODULES
from message_forwarding_bot.utils.loader import load_modules
from message_forwarding_bot.utils.telegram import tg_exceptions_handler

LOGGER = logging.getLogger(__name__)
BOT = Client(USERNAME, API_KEY, API_HASH)
BOT_INFO = {}


def main() -> None:
    BOT.run(run())


@tg_exceptions_handler
async def run() -> None:
    async with BOT:
        bot_info = await BOT.get_me()
        BOT_INFO.update(
            {"name": bot_info.first_name, "username": bot_info.username, "id": bot_info.id}
        )
        LOGGER.info(
            "Bot started as %s! Username is %s and ID is %s",
            BOT_INFO["name"],
            BOT_INFO["username"],
            BOT_INFO["id"],
        )
        load_modules(ALL_MODULES, __package__)
        await idle()
    await BOT.stop()


