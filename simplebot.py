# import asyncio
# import os
# from aiogram import Bot, Dispatcher
# from aiogram.types import Message
# from aiogram.filters import Command

# TOKEN = os.getenv("BOT_TOKEN")

# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# @dp.message(Command("start"))
# async def start_handler(message: Message):
#     await message.answer("Salom! Railway'dagi bot ishlayapti 🚄")

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())

import time

LAST_WELCOME_TIME = 0
WELCOME_INTERVAL = 3600  # 1 soat (sekundda)

import asyncio
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ChatType

# ====== CONFIG ======
TOKEN = os.getenv("BOT_TOKEN")

# Lokatsiya (o'zgartirishingiz mumkin)
LATITUDE = 41.453528
LONGITUDE = 69.566314

welcome_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="📜 Guruh qoidalari",
        url="https://t.me/arzonguruchchirchiq/2"
    )],
    [InlineKeyboardButton(
        text="⭐ Mamnun mijozlar fikrlari",
        url="https://t.me/arzonguruchchirchiq/3"
    )],
    [InlineKeyboardButton(
        text="ℹ️ Batafsil ma’lumot",
        url="https://t.me/arzonguruchchirchiq/4"
    )],
    [InlineKeyboardButton(
        text="📍 Locatsiya",
        url="https://t.me/arzonguruchchirchiq/16"
    )]
])

WELCOME_TEXT = (
    "👋 Xush kelibsiz!\n\n"
    "Quyidagi tugmalar orqali kerakli ma’lumotlarni olishingiz mumkin 👇"
)


# WELCOME_TEXT = (
#     "👋 Xush kelibsiz!\n"
#     "❌ Reklama va linklar taqiqlanadi\n"
#     "📍 'locatsiya' deb yozsangiz joylashuv yuboriladi"
# )

# ====== INIT ======
bot = Bot(token=TOKEN)
dp = Dispatcher()


# ====== HANDLER ======
@dp.message()
async def group_moderator(message: Message):
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

    # 1️⃣ Kirish xabarini o‘chirish + welcome
    if message.new_chat_members:
        await message.delete()

        global LAST_WELCOME_TIME

        current_time=time.time()

        if current_time - LAST_WELCOME_TIME < WELCOME_INTERVAL:
            return # hali 1 soat o'tmadi
        LAST_WELCOME_TIME=current_time

        user=message.new_chat_members[-1]

        await message.answer(
                f"{WELCOME_TEXT}\n\n👤 {user.full_name}",
                reply_markup=welcome_keyboard
            )
        return



    # 2️⃣ Chiqish xabarini o‘chirish
    if message.left_chat_member:
        await message.delete()
        return

    if not message.text:
        return

    text = message.text.lower()

    # 🔐 Admin tekshiruvi
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if member.status in ("administrator", "creator"):
        return

    # 3️⃣ HTTPS linklarni o‘chirish
    if "https://" in text:
        await message.delete()
        return

    # 4️⃣ Locatsiya yozib yuborilganda
    if text == "locatsiya" or text=="Locatsiya" or text=="manzil" or text=="Адрес" or text=="лакатса":
        await message.answer_location(LATITUDE, LONGITUDE)
        await message.answer(
        "📍 Bizning manzil:\n"
        "Toshkent viloyati, Chirchiq tumani\n"
        "🕘 Ish vaqti: 09:00 – 21:00\n"
        "📞 Aloqa: +998 91 777 44 43\n"
        "Sizni do'konimizda kutamiz"
    )
    return

# @dp.callback_query(F.data == "send_location")
# async def send_location_callback(call: CallbackQuery):
#     await call.message.answer_location(LATITUDE, LONGITUDE)
#     await call.answer()



# ====== START ======
async def main():
    await dp.start_polling(bot, allowed_updates=["message"])

if __name__ == "__main__":
    asyncio.run(main())
