from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot_base import session_maker, User
from sqlalchemy import select
# from lexicon.lexicon import LEXICON
# from database import users_db
# from servises import my_book


# async def new_kb(user_tg_id:int) -> InlineKeyboardMarkup:


async def create_keyboard(user_tg_id:int) -> InlineKeyboardMarkup:
    async with session_maker() as session:
        query = await session.execute(select(User).filter(User.id == user_tg_id))
        print('query =', query)
        n = query.scalar()
        print('needed_data = ', n)
        rest_att = n.attempts
        button_1 = InlineKeyboardButton(text=f'Количесвто оставшихся попыток  {rest_att}', callback_data='att')
        attempt_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[button_1]])
        return attempt_keyboard


# def create_three_button_kbd(user_id: int):
#     """ Возвращает инлайн клавиатуру пагинации """
#     page = users_db[user_id]["page"]
#     buttons = ['backward', f'{page}/{BOOK_LENGTH}', 'forward']
#     # для первой и последней страницы лишние кнопки не показываются
#     buttons = buttons[1:] if page == 1 else buttons[:-1] if page == BOOK_LENGTH else buttons
#     return create_pagination_keyboard(*buttons)

