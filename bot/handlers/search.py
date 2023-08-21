from telegram import Update
import telegram
from telegram.ext import ContextTypes

from bot.services.search import GoogleSearch
from bot.utils.keyboard import get_search_keyboard
from bot.utils.response import send_response
from bot.utils.templates import render_template


async def search_handler(update: Update, context: ContextTypes):
    search = GoogleSearch()
    results = await search.get_search_results(update.message.text)
    context.user_data["search_results"] = results
    current_result = results[0]
    current_index = 0

    await send_response(
        update,
        context,
        text=render_template(
            "search.j2",
            {
                "result_title": current_result[0],
                "result_url": current_result[1],
            },
        ),
        keyboard=get_search_keyboard(current_index, len(results)),
    )


async def search_button(update: Update, context: ContextTypes):
    callback_query = update.callback_query
    await callback_query.answer()

    results = context.user_data.get("search_results")
    current_index = int(callback_query.data[0])
    current_result = results[current_index]

    await callback_query.edit_message_text(
        text=render_template(
            "search.j2",
            {
                "result_title": current_result[0],
                "result_url": current_result[1],
            },
        ),
        parse_mode=telegram.constants.ParseMode.HTML,
        reply_markup=get_search_keyboard(current_index, len(results)),
    )
