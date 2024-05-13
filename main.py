import asyncio
from aiogram import Bot, Dispatcher
import game_handlers
import command_handlers
import callback_handlers
from bot_base import init_models
from bot_tocken import BOT_TOKEN
# Функция конфигурирования и запуска бота
async def main():
    await init_models()
    # Инициализируем бот и диспетчер
    bot = Bot(token=BOT_TOKEN,
              parse_mode='HTML')
    dp = Dispatcher()
    # Регистрируем роутеры в диспетчере
    dp.include_router(command_handlers.command_router)
    dp.include_router(game_handlers.game_router)
    dp.include_router(callback_handlers.cb_router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
