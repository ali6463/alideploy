from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menueng = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="๐Bots for example"),
            KeyboardButton(text="๐ก About Us"),

        ],
        [
            KeyboardButton(text="โTo order"),
            KeyboardButton(text="๐งพ Terms of offer"),

        ],
        [
            KeyboardButton(text="๐ง๐ปโ๐ป Contact the developer"),
        ],

    ],
    resize_keyboard=True
)

orqagaeng = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="๐Back"),

        ],

    ],
    resize_keyboard=True
)