import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from models import async_main
import random
import keyboard
import requests
from datetime import datetime
from sqlalchemy import create_engine


bot = Bot("<TOKEN>")
dp = Dispatcher()


class Reg(StatesGroup):
    infa = State()
    end = State()

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}! \nТыкай нужную тебе кнопочку', reply_markup=keyboard.main_kb)


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Если что-то плохо работает или у тебя есть идеи для доработки \nПиши сюда: https://t.me/knaz_vladimi ')


@dp.message(F.text == 'Запись достижений')
async def silk(message: Message, state: FSMContext):
    await state.set_state(Reg.infa)
    await message.answer('Напиши в одном предложении какое нибудь достижение за сегодня.'
                         'Помни, что даже самые маленькие шаги могут повлиять на будущее!')




@dp.message(Reg.infa)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(infa=message.text)
    data = await state.get_data()
    await message.answer(f'Ваау, ты молодец!')
    await requests.set_point(message.from_user.id, message.text)
    await state.clear()




@dp.message(F.text == 'Список достижений')
async def get_descripion(message: Message):
    s = ''
    for i in await requests.get_descrip(message.from_user.id):
        s += f"{i.description}\n"
    await message.answer(s)


@dp.message(F.text == 'Одно из достижений')
async def get_random(message: Message):
    a = [i for i in await requests.get_descrip(message.from_user.id)]
    rnum = random.choice(a)
    await message.reply(f'Совсем недавно ты сделал полезное дело! \n\n{rnum.description}')


@dp.message()
async def echo(message: Message):
    await message.answer(f'Ой, я тебя не понимаю. Попробуй нажать на кнопочку.')

async def main():
    await async_main()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
