from aiogram import Router
from filters import CALLBACK_FILTER, SHOW_FILTER
from bot_base import User, session_maker
from sqlalchemy import select
from lexicon import antwort, previous_told
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
cb_router = Router()


@cb_router.callback_query(CALLBACK_FILTER())
async def show_previous_tally(callback: CallbackQuery):
    print(f'callback_data= {callback.data}')
    user_id = callback.from_user.id
    async with session_maker() as session:
        query = await session.execute(select(User).filter(User.id == user_id))
        n = query.scalar()
        data = map(str, filter(None, (n.att_1, n.att_2, n.att_3, n.att_4, n.att_5)))
        arr_batt = [InlineKeyboardButton(text=x, callback_data='show') for x in data]
        await callback.message.edit_text(text=previous_told,
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[arr_batt]))
        await callback.answer()


@cb_router.callback_query(SHOW_FILTER())
async def other_tally(callback: CallbackQuery):
    await callback.message.edit_text(text=antwort,
                        reply_markup=None)
    await callback.answer()