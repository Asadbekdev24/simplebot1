

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



#TOKEN="8301952345:AAGSohy8NxNfiTuhu75kYzG7iR01Qep0dZg" beta test uchun api @yordamchi_beta_bot

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




# ====== INIT ======
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.new_chat_members)
async def welcome_handler(message: Message):
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

    await message.delete()

    global LAST_WELCOME_TIME
    current_time = time.time()

    if current_time - LAST_WELCOME_TIME < WELCOME_INTERVAL:
        return

    LAST_WELCOME_TIME = current_time
    user = message.new_chat_members[-1]

    await message.answer(
        f"{WELCOME_TEXT}\n\n👤 {user.full_name}",
        reply_markup=welcome_keyboard
    )


@dp.message(F.left_chat_member)
async def left_handler(message: Message):
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

    await message.delete()

@dp.message(F.text.contains("https://"))
async def delete_links(message: Message):
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if member.status in ("administrator", "creator"):
        return

    await message.delete()

LOCATION_WORDS = {
    "locatsiya", "manzil", "адрес", "лакатса"
}

PHOTO_ID = "AgACAgIAAyEFAASTZ0bCAAMlaWux39w8P6S_boSPyqygDEVCxV8AAtgMaxt6illLuMHCIBed8bMBAAMCAAN5AAM4BA"

@dp.message(F.text)
async def location_handler(message: Message):
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

    text = message.text.lower().strip()

    if text not in LOCATION_WORDS:
        return

    await message.answer_location(
        latitude=LATITUDE,
        longitude=LONGITUDE
    )

    await message.answer_photo(
        photo=PHOTO_ID,
        caption=(
            "📸 Bizning do'kon rasmi\n"
            "📍 Bizning manzil:\n"
            "Toshkent viloyati, Chirchiq shahri\n"
            "🕘 Ish vaqti: 09:00 – 21:00\n"
            "📞 Aloqa: +998 91 777 44 43\n"
            "Sizni do'konimizda kutamiz!"
        )
    )

# ====== START ======
async def main():
    await dp.start_polling(bot, allowed_updates=["message", "chat_member"])

if __name__ == "__main__":
    asyncio.run(main())
