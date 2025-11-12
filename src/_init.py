import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import Message


load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет! {html.bold('Ванпачман')} - бот, где вы сможете стать героем!")

@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer(f"Добавьте бота в чат.")


@dp.message(Command("fight"))
async def command_fight_handler(message: Message) -> None:
    await message.answer("бой")

@dp.message(Command("me"))
async def command_profile_handler(message: Message) -> None:
    await message.answer("Профиль")


@dp.message(Command("stats"))
async def command_stats_handler(message: Message) -> None:
    await message.answer("Статистика беседы")

@dp.message(Command("top"))
async def command_top_handler(message: Message) -> None:
    await message.answer("Топ во всех беседах")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())