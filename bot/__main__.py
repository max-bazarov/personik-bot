import logging

from telegram.ext import (ApplicationBuilder, CallbackQueryHandler,
                          CommandHandler, MessageHandler, filters)

from bot import config
from bot.handlers.search import search_button, search_handler
from bot.handlers.start import start_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


if not config.TELEGRAM_BOT_TOKEN:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN env variable " "wasn't implemented in .env"
    )


def main():
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CallbackQueryHandler(search_button))
    application.add_handler(MessageHandler(filters.TEXT, search_handler))

    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
