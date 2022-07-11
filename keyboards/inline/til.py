from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

til_sozlama = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="En", callback_data="ingiliz"),
            InlineKeyboardButton(text="Uz", callback_data="uzbek"),
        ],
    ]
)

zakaz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📞Dasturchi bilan bog'lanish", url="http://t.me/AlDevelopmentuz"),
        ],
    ]
)
aloqa = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧑🏻‍💻 Dasturchi bilan bog'lanish", url="http://t.me/AlDevelopmentuz"),

        ],
    ]
)
zakazeng = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📞Contact the developer", url="http://t.me/AlDevelopmentuz"),
        ],
    ]
)
aloqaeng = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧑🏻‍💻 Contact the developer", url="http://t.me/AlDevelopmentuz"),

        ],
    ]
)