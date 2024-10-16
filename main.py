import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(F.photo)
async def aitext(message: Message):
    list = ['ого какая фотка', ' что это такое', 'не отправляй мне это']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
@dp.message(F.text == 'Что такое ИИ')
async def aitext(message: Message):
    await message.answer('Это искусственный интеллект, который может вычислять настоящее время.')
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start - запуск бота \n /help - помощь')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello!')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())