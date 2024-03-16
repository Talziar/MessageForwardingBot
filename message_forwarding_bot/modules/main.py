"""Bot main module."""

from message_forwarding_bot.bot import BOT
from message_forwarding_bot import USER_ID
from message_forwarding_bot.utils.telegram import tg_exceptions_handler


@BOT.on_message()
@tg_exceptions_handler
async def start(client, message) -> None:
    await BOT.forward_messages(USER_ID, message.from_user.id, [message.id])
