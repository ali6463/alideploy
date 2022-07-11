from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menueng = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="🛒Bots for example"),
            KeyboardButton(text="💡 About Us"),

        ],
        [
            KeyboardButton(text="➕To order"),
            KeyboardButton(text="🧾 Terms of offer"),

        ],
        [
            KeyboardButton(text="🧑🏻‍💻 Contact the developer"),
        ],

    ],
    resize_keyboard=True
)

orqagaeng = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="🔙Back"),

        ],

    ],
    resize_keyboard=True
)