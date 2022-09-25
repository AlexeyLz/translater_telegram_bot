from aiogram import types


def get_keyboard_info_word(words, arguments):
    buttons = []
    for word in words:
        buttons.append(
            types.InlineKeyboardButton(text=word, callback_data="info_word_state_" + arguments + '_' + word), )

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard
