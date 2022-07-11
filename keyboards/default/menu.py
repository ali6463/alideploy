from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="🛒Namuna uchun botlar"),
            KeyboardButton(text="💡 Biz haqimizda"),

        ],
        [
            KeyboardButton(text="➕Buyurtma berish"),
            KeyboardButton(text="🧾 Oferta shartlari"),

        ],
        [
            KeyboardButton(text="🧑🏻‍💻 Dasturchi bilan bog'lanish"),

        ],

    ],
    resize_keyboard=True
)

orqaga = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="🔙Orqaga"),

        ],

    ],
    resize_keyboard=True
)