from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class DATA_IS_DIGIT(BaseFilter):
    async def __call__(self, message: Message):
        if message.text.isdigit() and 0 < int(message.text) < 100:
            return True
        return False


class CALLBACK_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'att':
            return True
        return False

class SHOW_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'show':
            return True
        return False