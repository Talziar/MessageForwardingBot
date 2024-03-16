from asyncio import sleep
from collections.abc import Callable
from functools import wraps
from typing import Any, cast

from pyrogram.errors import (
    ChannelPrivate,
    ChatWriteForbidden,
    FloodWait,
    InputUserDeactivated,
    InterdcCallError,
    MessageIdInvalid,
    MessageNotModified,
    UserIsBlocked,
    SlowmodeWait
)


def tg_exceptions_handler(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Callable[..., Any]:
        try:
            return cast(Callable[..., Any], await func(*args, **kwargs))
        except (
            ChannelPrivate,
            ChatWriteForbidden,
            UserIsBlocked,
            InterdcCallError,
            MessageNotModified,
            InputUserDeactivated,
            MessageIdInvalid,
        ):
            return lambda: None
        except SlowmodeWait as error:
            await sleep(error.value)
            return tg_exceptions_handler(await func(*args, **kwargs))
        except FloodWait as error:
            await sleep(error.value)
            return tg_exceptions_handler(await func(*args, **kwargs))

    return wrapper
