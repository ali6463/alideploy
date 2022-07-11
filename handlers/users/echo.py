from aiogram.types import Message

from data.config import ADMINS
from filters import IsPrivate
from loader import dp


# Echo bot
@dp.message_handler(IsPrivate(), state=None)
async def bot_echo(message: Message):
    await dp.bot.forward_message(chat_id=ADMINS[0], from_chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer("⚠ Siz noo‘rin buyruq kiritdingiz, tugmachalardan foydalaning!\n⚠ You have entered an invalid command, use the buttons!")