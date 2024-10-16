import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
import random
from config import TOKEN
from gtts import gTTS
import os
from googletrans import Translator

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()


@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)

@dp.message(Command('rvoice'))
async def rvoice(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'record_audio')
    voice = FSInputFile('voice.ogg')


@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile('tg.pdf')
    await bot.send_document(message.chat.id, doc)


@dp.message(Command('audio'))
async def audio(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_audio')
    audio = FSInputFile('audio.mp3')
    await bot.send_audio(message.chat.id, audio)

@dp.message(Command('training'))
async def training(message: Message):
    training_list = [
        "Тренировка 1:\n1. Лягте на пол лицом вниз и поднимитесь на локтях так, чтобы тело образовало прямую линию от головы до пяток.Удерживайте положение, напрягая мышцы пресса и ягодицы",
        "Тренировка 2:\n1. Стоитесь в положении лежа и смотрите в сторону.При этом никто не должен видеть вас.Удерживайте",
        "Тренировка 3:\n1. выдохните"
        ]
    rand_tr = random.choice(training_list)
    await message.answer(f"Это ваша мини тренировка на сегодня {rand_tr}")
    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('training.ogg')
    audio = FSInputFile('training.ogg')
    await bot.send_voice(message.chat.id, audio)
    os.remove('training.ogg')


@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('voice.ogg')
    await message.answer_voice(voice)





@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start - запуск бота \n /help - помощь')

@dp.message(Command('photo', prefix='!'))
async def photo(message: Message):
    list = ['https://i.pinimg.com/736x/ad/3e/c5/ad3ec54ecdcfefaa4eb5eddbd9f36555.jpg', 'https://i.pinimg.com/originals/af/1b/5d/af1b5d0bf3b2a189866925988f2f244d.jpg', 'https://www.zastavki.com/pictures/originals/2014/Nature___Seasons___Spring_Beautiful_flowers_in_the_spring_field_067765_.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(rand_photo, caption='это класс фотка')

@dp.message(F.photo)
async def aitext(message: Message):
    list = ['ого какая фотка', ' что это такое', 'не отправляй мне это']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')


@dp.message(F.text == 'Что такое ИИ')
async def aitext(message: Message):
    await message.answer('Это искусственный интеллект, который может вычислять настоящее время.')


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start - запуск бота \n /help - помощь')



@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Привет, {message.from_user.full_name}')

@dp.message()
async def translate_message(message: types.Message):
    translated = translator.translate(message.text, dest='en')
    await message.answer(f'Translation: {translated.text}')

@dp.message()
async def start(message: Message):
    if message.text.lower() == 'тест':
        await message.answer('Тест пройден')










async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())