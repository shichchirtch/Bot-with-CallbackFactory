from aiogram import Router
from aiogram.filters import CommandStart
from lexicon import start_greeding
from aiogram.types import Message, ReplyKeyboardRemove
from external_function import insert_new_user_in_table

command_router = Router()

@command_router.message(CommandStart())
async def process_start_command(message: Message):
    # Логируем старт Бота
    print(f'user {message.chat.first_name} press start')
    user_name = message.chat.first_name
    user_tg_id = message.from_user.id
    await insert_new_user_in_table(user_tg_id, user_name)
    await message.answer(
        f'Привет, {message.chat.first_name} !  \U0001F60A\n {start_greeding}',
                        reply_markup=ReplyKeyboardRemove())
    print("Process finfshed")
