import asyncio
import logging
import sys

# --------------------------------
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hide_link


# Initial Instaloader Commands
TOKEN = "6770289397:AAEH2Y6--p6n6NmFe42OtPYgr2vQgCKDexI"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command

    """


    await message.answer(f"Hello {message.from_user.first_name}")

    # message.reply(f"Welcome to InstaFetcher. click /fetch to get posts from {USER}")

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
