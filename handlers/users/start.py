import asyncio
from datetime import datetime

import aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from aiogram.types import Message

from keyboards.default.menu import menu
from keyboards.default.menueng import menueng
from keyboards.inline.til import til_sozlama
from loader import dp, bot
from states.datastate import Inputtil

rx=999999999999999*23432423432423324
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f"🇺🇸 Choose language\n🇺🇿 Tilni tanlang", reply_markup=til_sozlama)
    await Inputtil.Newtil.set()

@dp.callback_query_handler(state=Inputtil.Newtil, text="uzbek")
async def buy_mous(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    timeNow1 = datetime.now().strftime("%H:%M")
    await call.message.answer(f"<b>😊Assalomu alaykum</b>, {call.from_user.get_mention(as_html=True)}", reply_markup=menu)
    await state.finish()
    awdwad4 = await bot.send_message(chat_id=call.message.chat.id, text=f"⚙️Siz Bot yasash xizmatiga tashrif buyirdingiz<strong>\nBiz orqali murrakab yoki sodda, istalgan turdagi, har qanday tashkilot va yo'nalishga doir o'z telegram botingizga buyurtma berishingiz mumkin.</strong>\n\n• <i>Xizmat ko'rsatish vaqti</i> :<b>🕛 8:00 - 23:00</b> gacha\n• <em>Xozirgi vaqt :</em><b>⌚️ {timeNow1}</b>\n")
    await asyncio.sleep(1)
    for i in range(rx):
        try:
            timeNow = datetime.now().strftime("%H:%M")
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=awdwad4.message_id, text=f"⚙️Siz Bot yasash xizmatiga tashrif buyirdingiz<strong>\nBiz orqali murrakab yoki sodda, istalgan turdagi, har qanday tashkilot va yo'nalishga doir o'z telegram botingizga buyurtma berishingiz mumkin.</strong>\n\n• <i>Xizmat ko'rsatish vaqti</i> :<b>🕛 8:00 - 23:00</b> gacha\n• <em>Xozirgi vaqt :</em><b>⌚️ {timeNow}</b>\n")
            await asyncio.sleep(29)
        except aiogram.utils.exceptions.MessageNotModified:
            continue
        except aiogram.utils.exceptions.RetryAfter:
            pass


@dp.callback_query_handler(state=Inputtil.Newtil, text="ingiliz")
async def buy_mous(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.answer(cache_time=30)
    timeNow1 = datetime.now().strftime("%H:%M")
    await call.message.answer(f"<b>😊Hello</b>, {call.from_user.get_mention(as_html=True)}", reply_markup=menueng)
    await state.finish()
    awdwad4 = await bot.send_message(chat_id=call.message.chat.id, text=f"⚙️You have visited Bot Making Service<strong>\nThrough us, complex or simple, any type,\nown telegram for any profession \nyou can order your bot</strong>\n\n• <i>Service time</i> :<b>🕛 from 8:00 to 23:00</b>\n• <em>Present time :</em><b>⌚️ {timeNow1}</b>\n")
    await asyncio.sleep(1)
    for i in range(rx):
        try:
            timeNow = datetime.now().strftime("%H:%M")
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=awdwad4.message_id, text=f"⚙️You have visited Bot Making Service<strong>\nThrough us, complex or simple, any type,\nown telegram for any profession \nyou can order your bot</strong>\n\n• <i>Service time</i> :<b>🕛 from 8:00 to 23:00</b>\n• <em>Present time :</em><b>⌚️ {timeNow}</b>\n")
            await asyncio.sleep(29)
        except aiogram.utils.exceptions.MessageNotModified:
            continue
        except aiogram.utils.exceptions.RetryAfter:
            pass

@dp.message_handler(state=Inputtil.Newtil)
async def post_unknow(message: Message):
    await message.answer(text=f"🇺🇸 Choose language\n🇺🇿 Tilni tanlang", reply_markup=til_sozlama)
    await Inputtil.Newtil.set()