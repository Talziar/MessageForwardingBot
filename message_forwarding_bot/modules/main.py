"""Bot main module."""

from telethon import events

from message_forwarding_bot.bot import BOT
from message_forwarding_bot import USER_ID
from message_forwarding_bot.utils.telegram import tg_exceptions_handler


@BOT.on(events.NewMessage)
@tg_exceptions_handler
async def start(event: events.NewMessage.Event) -> None:
    await BOT.forward_messages(USER_ID, event.message)
