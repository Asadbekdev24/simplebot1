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