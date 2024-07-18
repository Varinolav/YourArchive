from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='Одно из достижений'),
            KeyboardButton(text='Список достижений')
        ],
        [
            KeyboardButton(text='Запись достижений')
        ]
    ],
    resize_keyboard=True, #размер кнопки
    input_field_placeholder='Ты сегодня такой молодец!!'
)
