from telegram import Update
from telegram.ext import ContextTypes

from bot.utils.response import send_response
from bot.utils.templates import render_template


async def start_handler(update: Update, context: ContextTypes):
    user_first_name = update.effective_user.first_name

    await send_response(
        update,
        context,
        text=render_template("start.j2", {'first_name': user_first_name}),
    )
