from aiogram import Router
from filters import DATA_IS_DIGIT
from keyboards import create_keyboard
from lexicon import antwort, no_att_lost, new_game
from aiogram.types import Message
from external_function import reset, update_table, check_attempts_lost_number
import asyncio
game_router = Router()

@game_router.message(DATA_IS_DIGIT())
async def process_numbers_answer(message: Message):
    user_tg_id = message.from_user.id
    user_name = message.chat.first_name
    if await check_attempts_lost_number(user_tg_id):
            print(f'\n Attempts for {user_name} = 0 Game done !')
            await reset(user_tg_id)  # обнуляю таблицу
            await message.answer(text=f'{user_name} {antwort}')
            await asyncio.sleep(1)
            await message.answer(text=no_att_lost)
            await message.answer(text=new_game,
                                 reply_markup= await create_keyboard(user_tg_id))
    else:
        await update_table(user_tg_id, int(message.text))
        await message.answer(text=f'{user_name} {antwort}',
                             reply_markup= await create_keyboard(user_tg_id))



