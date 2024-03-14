"""Telegram Bot."""

import asyncio
import json
import logging
from pathlib import Path

from telethon.sync import TelegramClient

from message_forwarding_bot import API_HASH, API_KEY
from message_forwarding_bot.modules import ALL_MODULES
from message_forwarding_bot.utils.loader import load_modules

LOGGER = logging.getLogger(__name__)
BOT = TelegramClient("message_forwarding_bot", API_KEY, API_HASH)
BOT.start()
BOT.parse_mode = "markdown"
BOT_INFO = {}


def main() -> None:
    """Main."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


async def run() -> None:
    """Run the bot."""
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
    # Check if the bot is restarting
    if Path("restart.json").exists():
        restart_message = json.loads(Path("restart.json").read_text())
        await BOT.edit_message(
            restart_message["chat"],
            restart_message["message"],
            "Restarted Successfully!",
        )
        Path("restart.pickle").unlink()
    async with BOT:
        await BOT.run_until_disconnected()