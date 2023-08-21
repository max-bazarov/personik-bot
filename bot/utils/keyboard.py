from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_search_keyboard(
    current_index: int, results_count: int
) -> InlineKeyboardMarkup:
    next_index = current_index + 1
    if next_index > results_count - 1:
        next_index = 0

    keyboard = [
        [
            InlineKeyboardButton(
                "Показать следующий результат",
                callback_data=next_index,
            ),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
