import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
import ssl
from bot import middlewares, handlers, filters
from bot import config
from bot.services import commands_setter, admin_notificator, logger
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        f"{config.BASE_WEBHOOK_URL}{config.WEBHOOK_PATH}",
        secret_token=config.WEBHOOK_SECRET,
    )
    await admin_notificator.notify(bot)


def main() -> None:
    dp = Dispatcher()
    dp.startup.register(on_startup)
    bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    filters.setup(dp)
    middlewares.setup(dp)
    handlers.setup(dp)

    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=config.WEBHOOK_SECRET,
    )

    webhook_requests_handler.register(app, path=config.WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=config.WEBHOOK_HOST, port=config.WEBHOOK_PORT)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
