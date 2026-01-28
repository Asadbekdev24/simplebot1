
import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ChatType
from aiogram.client.default import DefaultBotProperties

# ====== CONFIG ======
TOKEN = os.getenv("BOT_TOKEN")
#TOKEN="8301952345:AAGSohy8NxNfiTuhu75kYzG7iR01Qep0dZg"
LATITUDE = 41.453528
LONGITUDE = 69.566314
# Global o'zgaruvchini funksiya ichida saqlash xotira uchun yaxshiroq
LAST_WELCOME_TIME = 0
WELCOME_INTERVAL = 3600

# Keyboardni doimiy (constant) qilib belgilash
WELCOME_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📜 Guruh qoidalari", url="https://t.me/arzonguruchchirchiq/2")],
    [InlineKeyboardButton(text="⭐ Mamnun mijozlar fikrlari", url="https://t.me/arzonguruchchirchiq/3")],
    [InlineKeyboardButton(text="ℹ️ Batafsil ma’lumot", url="https://t.me/arzonguruchchirchiq/4")],
    [InlineKeyboardButton(text="📍 Locatsiya", url="https://t.me/arzonguruchchirchiq/16")]
])

UNALLOWED_WORDS = {"aksiya", "ehson", "hujjat", "daromad"}
LOCATION_WORDS = {"locatsiya", "manzil", "адрес", "лакатса", "adres"}
PHOTO_ID = "AgACAgIAAyEFAASTZ0bCAAMlaWux39w8P6S_boSPyqygDEVCxV8AAtgMaxt6illLuMHCIBed8bMBAAMCAAN5AAM4BA"

# ====== INIT ======
# parse_mode kabi narsalarni default qilish RAMni tejaydi (har safar ob'ekt yaratilmaydi)
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

# Handlerlarni optimallashtirish: Adminlarni tekshirish funksiyasini kesh bilan ishlatsa bo'ladi
async def is_admin(message: Message):
    member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
    return member.status in ("administrator", "creator")

@dp.message(F.new_chat_members)
async def welcome_handler(message: Message):
    global LAST_WELCOME_TIME
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

    try:
        await message.delete()
    except: pass

    import time
    current_time = time.time()
    if current_time - LAST_WELCOME_TIME < WELCOME_INTERVAL:
        return

    LAST_WELCOME_TIME = current_time
    user = message.new_chat_members[-1]
    await message.answer(
        f"👋 Xush kelibsiz!\n\nQuyidagi tugmalar orqali ma’lumot oling 👇\n\n👤 <b>{user.full_name}</b>",
        reply_markup=WELCOME_KEYBOARD
    )

@dp.message(F.left_chat_member)
async def left_handler(message: Message):
    if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        try: await message.delete()
        except: pass

@dp.message(F.text)
async def message_filter(message: Message):
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

    text = message.text.lower().strip()

    # Reklama va Linklarni tekshirish (Bitta handlerga birlashtirildi - RAM tejash uchun)
    if any(word in text for word in UNALLOWED_WORDS) or "https://" in text:
        if not await is_admin(message):
            await message.delete()
            return

    # Lokatsiya so'zlarini tekshirish
    if text in LOCATION_WORDS:
        await message.answer_location(latitude=LATITUDE, longitude=LONGITUDE)
        await message.answer_photo(
            photo=PHOTO_ID,
            caption="📸 Bizning do'kon rasmi\n"
            "📍 Bizning manzil:\n"
            "Toshkent viloyati, Chirchiq shahri\n"
            "🕘 Ish vaqti: 09:00 – 21:00\n"
            "📞 Aloqa: +998 91 777 44 43\n"
            "Sizni do'konimizda kutamiz!"
        )

# ====== START ======
async def main():
    # Eng muhim qism: Keraksiz update turlarini o'chirib qo'yamiz
    # Faqat message va chat_member ni qabul qilamiz
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=["message"])

if __name__ == "__main__":
    asyncio.run(main())




