import configparser
import logging
from new_main import find
from aiogram import Bot, Dispatcher, executor, types

cfg = configparser.ConfigParser()
cfg.read("config.ini")
API_TOKEN = cfg.get("main", "token")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ помощник в игре 5букв.\nПомогу тебе найти слово.")
    await message.answer("\u2705 Напишите найденные буквы, остальные буквы поставьте точкой. Например: .а.к.")

@dp.message_handler()
async def echo(message: types.Message):
    global good, maybe, bad, i
    if i % 3 == 0:
        good = message.text
        await message.answer('\u2753 Напишите буквы не на своем месте. Если таких нету, отправьте точку ')
        i += 1
    elif i % 3 == 1:
        maybe = message.text
        await message.answer('\u274C Напишите плохие буквы ')
        i += 1
    else:
        bad = message.text
        await message.answer(find(good, maybe, bad))
        i += 1
        await message.answer("\u2705 Напишите найденные буквы, остальные буквы поставьте точкой. Например: .а.к.")

if __name__ == '__main__':
    i = 0
    good = '.'
    maybe = ''
    bad = ''
    executor.start_polling(dp, skip_updates=True)
