import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types.message import Message

bot = Bot(token=os.getenv("TESTS_TOKEN_API"))
dp = Dispatcher()

SYSTEM_MESSAGES = (
    F.pinned_message
    | F.new_chat_title
    | F.new_chat_photo
    | F.delete_chat_photo
    | F.new_chat_members
    | F.left_chat_member
    | F.migrate_to_chat_id
    | F.migrate_from_chat_id
    | F.video_chat_started
    | F.video_chat_ended
    | F.video_chat_scheduled
    | F.video_chat_participants_invited
)

@dp.message(SYSTEM_MESSAGES)
async def cmd_del(message: Message) -> None:
    try:
        await message.delete()
    except Exception as e:
        print(f"Error: {e}")

async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped.")