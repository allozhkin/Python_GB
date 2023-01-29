from create import dp
from aiogram import types
from random import randint, shuffle


total = 300


@dp.message_handler(commands=['start'])
async def mess_start(message: types.Message):
    await message.answer('Введите /help для информации')
    await message.answer(f'Добро пожаловать в игру, {message.from_user.first_name}')
    await message.answer(f'На столе лежит {total} конфет,\n За один ход можно забрать не более чем 28 конфет')
    await message.answer('Победит тот, кто заберет последние конфеты')
    await message.answer('Если хотите изменить количество конфет, введите /set количество конфет')


@dp.message_handler(commands=['set'])
async def mess_settings(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'Теперь на столе {total} конфет')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(f'/start: Начать игру\n/set : Установить количество конфет\n/help: узнать команды\n/exit: для выхода')


@dp.message_handler(commands=['exit'])
async def exit_command(message: types.Message):
    await message.answer('Пока')
    exit()


@dp.message_handler()
async def mess_all(message: types.Message):
    global total
    if message.text.isdigit():
        if int(message.text) > 28:
            await message.answer('Введите число от 1 до 28')
        else:
            total -= int(message.text)
    else:
        await message.answer('Введите число от 1 до 28')
    await message.answer(f'На столе осталось {total} конфет')

    if total <= 0:
        await message.answer('Победа!')
        exit()