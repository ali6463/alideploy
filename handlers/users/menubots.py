from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default.menu import menu, orqaga
from keyboards.default.menueng import orqagaeng, menueng
from keyboards.inline.til import aloqa, aloqaeng, zakazeng, zakaz
from loader import dp


@dp.message_handler(text="🔙Orqaga")
async def anseawawdadr_2blok(message: Message):
    await message.answer("✨Asosiy oyna", reply_markup=menu)

@dp.message_handler(text="🔙Back")
async def andr_2blok(message: Message):
    await message.answer("✨Main window", reply_markup=menueng)

@dp.message_handler(text="🧾 Oferta shartlari")
async def start_fanawlar(message: Message):
    await message.answer("<b>Oferta shartlari :</b>\n<em>• Bot buyurtma berish uchun dasturchi bilan bog'lanishdan oldin siz nima istashingizni aniqlashtirib oling!\n• Qanday bot kerakligini iloji boricha namuna orqali yoki batafsil tavfislab bering, bot dasturlash vaqtida ortiqcha muammo bo'lmasligi uchun.\n• Serverga joylab berish xizmati bepul, lekin server to'lov sizning xisozbingizdan bo'ladi, shu yerda server haqida qisqacha ma'lumot berib o'taman. Server bu telegrambot , web sayt yoki ilovalarni doimiy ishlashini ta'minlovchi xizmat, serversiz botingiz ishlamaydi. Server to'lovlari mijoz tomonidan amalga oshiriladi. Serverga to'lovlar oylik yoki yillik ko'rinishda to'lanadi.\n• Firibgarlik, Beodob mavzudagi telegram botlar yasash bo'yicha murojat ham qilib o'tirmang.\n• Xizmat uchun to'lovlar: Payme, Click, Apelsin, Karta orqali pul o'tkazmalar, Qiwi, USDT, Master Card\n• Bot buyurtma bergach, botning 20% qismi tayyor bulgach oldindan, xizmat haqining 10%-50% bo'lgan miqdorda to'lovni amalga oshirishi shart!\n• Savdo telegram botlari yoki shu turdagi botlar uchun 'To'lov tizimi'ni kiritish uchun Yuridik shaxs yoki tadbirkorlik hujjati talab qilinadi!</em>", reply_markup=orqaga)

@dp.message_handler(text="🧾 Terms of offer")
async def staret_fanawlar(message: Message):
    await message.answer("<b>Conditions of the offer:</b>\n<em>• Before contacting the developer to order a bot, clarify what you want!\n• Describe what kind of bot you need as much as possible by example or in detail, during bot programming so as not to cause too much trouble.\n• The server hosting service is free, but the server fee will be from your account, here I will give a brief information about the server. A server is a service that ensures the constant operation of telegrambot, website or applications, without a server your bot will not work. Server fees are paid by the client. Payments to the server are paid monthly or annually.\n• Don't even ask about creating telegram bots with fraudulent, obscene topics.\n• Payments for the service: Payme, Click, Orange, Card via money transfers, Qiwi, USDT, Master Card\n• After placing an order, the bot must pay 10%-50% of the service fee in advance when 20% of the bot is ready!\n• Trade telegram bots or Legal entity or business document is required to enter 'Payment system' for bots of type!</em>", reply_markup=orqagaeng)

@dp.message_handler(text="🛒Namuna uchun botlar")
async def st34art_fanawlar(message: Message):
    await message.answer("<b>🛒Namuna uchun botlar👇 :</b>\n\n●  @AlDevelopmentbot | <b>10$</b> dan <b>30$</b> gacha.\n●  @mandat_2022bot | <b>80$</b> dan <b>600$</b> gacha.\n●  @dtdtaxibot | <b>40$</b> dan <b>300$</b> gacha.\n●  @Oriflameorg_bot | <b>30$</b> dan <b>90$</b> gacha.\n●  @DurgerKingBot | <b>60$</b> dan <b>700$</b> gacha.\n●  @papayesbot | <b>45$</b> dan <b>400$</b> gacha.\n●  @tbc_uz_bot | <b>20$</b> dan <b>50$</b> gacha.\n●  @roboshopuzbot | <b>40$</b> dan <b>100$</b> gacha.\n●  @osonaptekabot | <b>100$</b> dan <b>400$</b> gacha.\n●  @stipendiya_edubot | <b>60$</b> dan <b>300$</b> gacha.\n●  @NovqaKursBot | <b>50$</b> dan <b>180$</b> gacha.\n●  @BepulDarslarBot | <b>40$</b> dan <b>100$</b> gacha.\n\n<strong>Yuqoridagi narxlar buyurtma bermoqchi bo'lgan botingiz imkonyatlari va bajaradigan funksiyalariga qarab narx belgilanadi!\nBu botlar sizga namuna sifatida ko'rsatilmoqda, bizni imkonyatimiz cheklanmagan , siz istagan har qanday botlarni yasab berolamiz. Buyutma berish uchun dasturchi bilan bog'laning.</strong>", reply_markup=orqaga)

@dp.message_handler(text="🛒Bots for example")
async def st364art_fanawlar(message: Message):
    await message.answer("<b>🛒Sample bots👇 :</b>\n\n● @AlDevelopmentbot | From <b>$10</b> to <b>$30</b>.\n● @mandat_2022bot | From <b>$80</b> to <b>$600</b>.\n● @dtdtaxibot | From <b>$40</b> to <b>$300</b>.\n● @Oriflameorg_bot | From <b>$30</b> to <b>$90</b>.\n● @DurgerKingBot | From <b>$60</b> to <b>$700</b>.\n● @papayesbot | From <b>$45</b> to <b>$400</b>.\n● @tbc_uz_bot | From <b>$20</b> to <b>$50</b>.\n● @roboshopuzbot | From <b>$40</b> to <b>$100</b>.\n● @osonaptekabot | From <b>$100</b> to <b>$400</b>.\n● @stipendiya_edubot | From <b>$60</b> to <b>$300</b>.\n● @NovqaKursBot | From <b>$50</b> to <b>$180</b>.\n● @BepulDarslarBot | From <b>$40</b> to <b>$100</b>.\n\n<strong>The above prices are based on the capabilities and functions of the bot you want to order!\nThese bots are for you as an example is showing, we are unlimited, we can make any bots you want. Contact the developer to order.</strong>", reply_markup=orqagaeng)


@dp.message_handler(text="💡 Biz haqimizda")
async def s4art_fanawlar(message: Message):
    photo_id1 = "AgACAgIAAxkBAAEQpO5ivrpog5HtvxTzdaz9dwoVYAuARgAC5LkxG7n2-Un97tiCgLCuEgEAAwIAA3MAAykE"
    await message.reply_photo(photo_id1, caption="<em>Biz ancha yillik tajribaga ega bo'lgan dasturchilar jamoasimiz.\nSizga o'z sifatli dasturiy mahsulotlarimzini tavsiya etolamiz. Sifat, creativ g'oyalar va qulay narx bizning asosiy ustuvor tomonimiz!\nJamoamiz tomonidan yaratilgan botlar insonlarning biznesiga muvaffaqiyat va muamolariga tezkor yechim bo'lib kelmoqda.</em>", reply_markup=orqaga)


@dp.message_handler(text="💡 About Us")
async def s4art_fanawlar(message: Message):
    photo_id1 = "AgACAgIAAxkBAAEQpO5ivrpog5HtvxTzdaz9dwoVYAuARgAC5LkxG7n2-Un97tiCgLCuEgEAAwIAA3MAAykE"
    await message.reply_photo(photo_id1, caption="<em>We are a team of programmers with many years of experience.\nWe recommend our quality software products to you. Quality, creative ideas and affordable price are our main priority!\nThe bots created by our team are becoming a quick solution to people's business success and problems.</em>", reply_markup=orqagaeng)

@dp.message_handler(text="🧑🏻‍💻 Dasturchi bilan bog'lanish")
async def s4a765rt_fanawlar(message: Message):
    photoid ="https://www.narzullayev.uz/uploads/photo_1652551896897.jpg"
    timeNow2 = datetime.now().strftime("%H:%M")
    try:
        old = int(timeNow2[0:2])
    except ValueError:
        old = int(timeNow2[0:1])
    if old >= 8 and old < 23:
        await dp.bot.send_photo(chat_id=message.chat.id, photo=photoid, caption="<b>Dasturchi bilan aloqaga chiqishdan oldin </b><u>🧾 Oferta shartlari</u><b> ni o'qib chiqing!</b>\n\n• <i>Xizmat ko'rsatish vaqti</i> :<b>🕛 8:00 - 23:00</b> gacha", reply_markup=aloqa)
    else:
        await message.answer("<strong>Dasturchining ish vaqti </strong>:🕛 8:00 - 23:00 gacha\n<em>Iltimos shu vaqt oralig'ida dasturchi bilan qayta aloqaga chiqing!</em>")

@dp.message_handler(text="🧑🏻‍💻 Contact the developer")
async def s4a76sadefs5rt_fanawlar(message: Message):
    photoid ="https://www.narzullayev.uz/uploads/photo_1652551896897.jpg"
    timeNow2 = datetime.now().strftime("%H:%M")
    try:
        old = int(timeNow2[0:2])
    except ValueError:
        old = int(timeNow2[0:1])
    if old >= 8 and old < 23:
        await dp.bot.send_photo(chat_id=message.chat.id, photo=photoid, caption="<b>Please read the </b><u>🧾 Offer Terms</u><b> before contacting the developer!</b>\n\n• <i>Service Time </i> :<b>🕛 from 8:00 to 23:00</b>", reply_markup=aloqaeng)
    else:
        await message.answer("<strong>Working hours of the developer </strong>:🕛 from 8:00 - 23:00\n<em>Please contact the developer again during this time!</em>")

@dp.message_handler(text="➕To order")
async def s4a765fsrt_fanawlar(message: Message):
    photoid ="https://www.narzullayev.uz/uploads/photo_1652551896897.jpg"
    timeNow2 = datetime.now().strftime("%H:%M")
    try:
        old = int(timeNow2[0:2])
    except ValueError:
        old = int(timeNow2[0:1])
    if old >= 8 and old < 23:
        await dp.bot.send_photo(chat_id=message.chat.id, photo=photoid, caption="<b>To order a Telegram bot, contact the developer\nPlease read the </b><u>🧾 Terms of Offer</u><b> before contacting the developer!</b>\n \n• <i>Service hours</i> :<b>🕛 from 8:00 to 23:00</b>", reply_markup=zakazeng)
    else:
        await message.answer("<strong>Order receiving time</strong>:🕛from 8:00 - 23:00\n<em>Please contact the developer again during this time!</em>")

@dp.message_handler(text="➕Buyurtma berish")
async def s4a7s65rt_fanawlar(message: Message):
    photoid ="https://www.narzullayev.uz/uploads/photo_1652551896897.jpg"
    timeNow2 = datetime.now().strftime("%H:%M")
    try:
        old = int(timeNow2[0:2])
    except ValueError:
        old = int(timeNow2[0:1])
    if old >= 8 and old < 23:
        await dp.bot.send_photo(chat_id=message.chat.id, photo=photoid, caption="<b>Telegram bot buyurtma berish uchun dasturchi bilan bog'laning\nDasturchi bilan aloqaga chiqishdan oldin </b><u>🧾 Oferta shartlari</u><b> ni o'qib chiqing!</b>\n\n• <i>Xizmat ko'rsatish vaqti</i> :<b>🕛 8:00 - 23:00</b> gacha", reply_markup=zakaz)
    else:
        await message.answer("<strong>Buyutma qabul qilish vaqti </strong>:🕛 8:00 - 23:00 gacha\n<em>Iltimos shu vaqt oralig'ida dasturchi bilan qayta aloqaga chiqing!</em>")