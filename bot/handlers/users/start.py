import time

from aiogram import types, Dispatcher
from aiogram.filters import CommandStart, Command
from bot import keyboards
import tools


async def start_handler(message: types.Message):
    msg_text = await tools.filer.read_txt("start")
    print(message.from_user.id)
    await message.answer(
        "Start"
    )

    await message.answer(
        "End"
    )


def setup(dp: Dispatcher):
    dp.message.register(start_handler, CommandStart())
