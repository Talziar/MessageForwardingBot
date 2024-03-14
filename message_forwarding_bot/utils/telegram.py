from asyncio import sleep
from collections.abc import Callable
from functools import wraps
from typing import Any, cast

from telethon import events
from telethon.errors import (
    ChannelPrivateError,
    ChatWriteForbiddenError,
    FloodWaitError,
    InputUserDeactivatedError,
    InterdcCallErrorError,
    MessageIdInvalidError,
    MessageNotModifiedError,
    SlowModeWaitError,
    UserIsBlockedError,
)
from telethon.tl.types import User


def tg_exceptions_handler(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Callable[..., Any]:
        try:
            return cast(Callable[..., Any], await func(*args, **kwargs))
        except (
            ChannelPrivateError,
            ChatWriteForbiddenError,
            UserIsBlockedError,
            InterdcCallErrorError,
            MessageNotModifiedError,
            InputUserDeactivatedError,
            MessageIdInvalidError,
        ):
            return lambda: None
        except SlowModeWaitError as error:
            await sleep(error.seconds)
            return tg_exceptions_handler(await func(*args, **kwargs))
        except FloodWaitError as error:
            await sleep(error.seconds)
            return tg_exceptions_handler(await func(*args, **kwargs))

    return wrapper
