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



#TOKEN="8301952345:AAGSohy8NxNfiTuhu75kYzG7iR01Qep0dZg"

#beta test uchun api @yordamchi_beta_bot

# @dp.message()
# async def group_moderator(message: Message):
#     if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
#         return

#     # 1️⃣ Kirish xabarini o‘chirish + welcome
#     if message.new_chat_members:
#         await message.delete()

#         global LAST_WELCOME_TIME

#         current_time=time.time()

#         if current_time - LAST_WELCOME_TIME < WELCOME_INTERVAL:
#             return # hali 1 soat o'tmadi
#         LAST_WELCOME_TIME=current_time

#         user=message.new_chat_members[-1]

#         await message.answer(
#                 f"{WELCOME_TEXT}\n\n👤 {user.full_name}",
#                 reply_markup=welcome_keyboard
#             )
#         return



#     # 2️⃣ Chiqish xabarini o‘chirish
#     if message.left_chat_member:
#         await message.delete()
#         return

#     if not message.text:
#         return

#     text = message.text.lower()

#     # 🔐 Admin tekshiruvi
#     member = await bot.get_chat_member(message.chat.id, message.from_user.id)
#     if member.status in ("administrator", "creator"):
#         return

#     # 3️⃣ HTTPS linklarni o‘chirish
#     if "https://" in text:
#         await message.delete()
#         return

#     # 4️⃣ Locatsiya yozib yuborilganda
#     if text == "locatsiya" or text=="Locatsiya" or text=="manzil" or text=="Адрес" or text=="лакатса" or text=="Manzil":
#         await message.answer_location(LATITUDE, LONGITUDE)
#     #     await message.answer(
#     #     "📍 Bizning manzil:\n"
#     #     "Toshkent viloyati, Chirchiq shahri\n"
#     #     "🕘 Ish vaqti: 09:00 – 21:00\n"
#     #     "📞 Aloqa: +998 91 777 44 43\n"
#     #     "Sizni do'konimizda kutamiz"
#     # )
#         PHOTO_ID = "AgACAgIAAyEFAASTZ0bCAAMlaWux39w8P6S_boSPyqygDEVCxV8AAtgMaxt6illLuMHCIBed8bMBAAMCAAN5AAM4BA"

#         await message.answer_photo(
#          photo=PHOTO_ID,
#          caption="📸 Bizning do'kon rasmi\n"
#         "📍 Bizning manzil:\n"
#         "Toshkent viloyati, Chirchiq shahri\n"
#         "🕘 Ish vaqti: 09:00 – 21:00\n"
#         "📞 Aloqa: +998 91 777 44 43\n"
#         "Sizni do'konimizda kutamiz!" )








# WELCOME_TEXT = (
#     "👋 Xush kelibsiz!\n"
#     "❌ Reklama va linklar taqiqlanadi\n"
#     "📍 'locatsiya' deb yozsangiz joylashuv yuboriladi"
# )




# ====== HANDLER ======

# photo_id ni aniqlash uchun kod
# @dp.message()
# async def get_photo_id(message: Message):
#     if message.photo:
#         await message.answer(
#             f"photo_id:\n<code>{message.photo[-1].file_id}</code>",
#             parse_mode="HTML"
#         )




    # photo = FSInputFile("photo.jpg")  # rasm bot papkasida bo‘lishi kerak
    # await message.answer_photo(
    #     photo=photo,
    #     caption="📸 Bizning ofis"
    # )
    # return

# @dp.callback_query(F.data == "send_location")
# async def send_location_callback(call: CallbackQuery):
#     await call.message.answer_location(LATITUDE, LONGITUDE)
#     await call.answer()




# aiofiles==25.1.0
# aiogram==3.24.0
# aiohappyeyeballs==2.6.1
# aiohttp==3.13.3
# aiosignal==1.4.0
# annotated-types==0.7.0
# attrs==25.4.0
# certifi==2026.1.4
# frozenlist==1.8.0
# idna==3.11
# magic-filter==1.0.12
# multidict==6.7.0
# propcache==0.4.1
# pydantic==2.12.5
# pydantic_core==2.41.5
# typing-inspection==0.4.2
# typing_extensions==4.15.0
# yarl==1.22.0



# import time

# LAST_WELCOME_TIME = 0
# WELCOME_INTERVAL = 3600  # 1 soat (sekundda)

# import asyncio
# import os
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message
# from aiogram.enums import ChatType

# # ====== CONFIG ======
# TOKEN = os.getenv("BOT_TOKEN")


# # Lokatsiya (o'zgartirishingiz mumkin)
# LATITUDE = 41.453528
# LONGITUDE = 69.566314

# welcome_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(
#         text="📜 Guruh qoidalari",
#         url="https://t.me/arzonguruchchirchiq/2"
#     )],
#     [InlineKeyboardButton(
#         text="⭐ Mamnun mijozlar fikrlari",
#         url="https://t.me/arzonguruchchirchiq/3"
#     )],
#     [InlineKeyboardButton(
#         text="ℹ️ Batafsil ma’lumot",
#         url="https://t.me/arzonguruchchirchiq/4"
#     )],
#     [InlineKeyboardButton(
#         text="📍 Locatsiya",
#         url="https://t.me/arzonguruchchirchiq/16"
#     )]
# ])

# WELCOME_TEXT = (
#     "👋 Xush kelibsiz!\n\n"
#     "Quyidagi tugmalar orqali kerakli ma’lumotlarni olishingiz mumkin 👇"
# )




# # ====== INIT ======
# bot = Bot(token=TOKEN)
# dp = Dispatcher()


# @dp.message(F.new_chat_members)
# async def welcome_handler(message: Message):
#     if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
#         return

#     await message.delete()

#     global LAST_WELCOME_TIME
#     current_time = time.time()

#     if current_time - LAST_WELCOME_TIME < WELCOME_INTERVAL:
#         return

#     LAST_WELCOME_TIME = current_time
#     user = message.new_chat_members[-1]

#     await message.answer(
#         f"{WELCOME_TEXT}\n\n👤 {user.full_name}",
#         reply_markup=welcome_keyboard
#     )


# @dp.message(F.left_chat_member)
# async def left_handler(message: Message):
#     if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
#         return

#     await message.delete()


# UNALLOWED_WORDS={
#     "aksiya", "ehson", "hujjat", "daromad",
# }

# @dp.message(F.text.lower().strip().in_(UNALLOWED_WORDS))
# async def delete_ads(message:Message):
#     if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
#         return
#     member = await bot.get_chat_member(message.chat.id, message.from_user.id)
#     if member.status in ("administrator", "creator"):
#         return

#     await message.delete()


# @dp.message(F.text.contains("https://"))
# async def delete_links(message: Message):
#     if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
#         return

#     member = await bot.get_chat_member(message.chat.id, message.from_user.id)
#     if member.status in ("administrator", "creator"):
#         return

#     await message.delete()



# LOCATION_WORDS = {
#     "locatsiya", "manzil", "адрес", "лакатса", "adres"
# }

# PHOTO_ID = "AgACAgIAAyEFAASTZ0bCAAMlaWux39w8P6S_boSPyqygDEVCxV8AAtgMaxt6illLuMHCIBed8bMBAAMCAAN5AAM4BA"

# @dp.message(F.text.lower().strip().in_(LOCATION_WORDS))
# async def location_handler(message: Message):
#     if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
#         return

#     text = message.text.lower().strip()

#     if text not in LOCATION_WORDS:
#         return

#     await message.answer_location(
#         latitude=LATITUDE,
#         longitude=LONGITUDE
#     )

#     await message.answer_photo(
#         photo=PHOTO_ID,
#         caption=(
#             "📸 Bizning do'kon rasmi\n"
#             "📍 Bizning manzil:\n"
#             "Toshkent viloyati, Chirchiq shahri\n"
#             "🕘 Ish vaqti: 09:00 – 21:00\n"
#             "📞 Aloqa: +998 91 777 44 43\n"
#             "Sizni do'konimizda kutamiz!"
#         )
#     )

# # ====== START ======
# async def main():
#     await dp.start_polling(bot, allowed_updates=["message", "chat_member"])

# if __name__ == "__main__":
#     asyncio.run(main())