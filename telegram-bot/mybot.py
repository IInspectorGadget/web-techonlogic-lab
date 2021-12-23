import base64
import io
import requests
import psycopg2
from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token="2113039370:AAFaleJ-uHr-1Fhj_AEaDKyaEeHoDHoEKkM")
dp = Dispatcher(bot, storage=storage)

userIsAut = False

def check_user_auth(user_id):
    global userIsAut
    try: 
        conn = psycopg2.connect(dbname='hello_django_dev', user='hello_django', 
                        password='hello_django', host='db', port = '5432')
    except:
        return False
    cursor = conn.cursor()
    sql = "SELECT * FROM userprofile_telegram WHERE telegram_id = '%s'" % user_id
    cursor.execute(sql)
    f = cursor.fetchall()
    if len(f) > 0:
        userIsAut = True
    else:
        userIsAut = False 


async def on_startup(_):
    print("Bot start")


class CreateNews(StatesGroup):
    title = State()
    small_text = State()
    image = State()
    text = State()

@dp.message_handler(commands=['create','/create'], state=None)
async def command_start(message: types.Message):
    check_user_auth(message.from_user.id)
    if userIsAut:
        await CreateNews.title.set()
        await bot.send_message(message.from_user.id, "Введите загаловок:", reply_markup=thirdMenu)
    else:
        await bot.send_message(message.from_user.id, "Вы должны авторезироваться", reply_markup=mainMenu)

@dp.message_handler(state="*", commands = 'отмена')
@dp.message_handler(Text(equals='отмена', ignore_case = True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, "OK", reply_markup=fourthMenu)

@dp.message_handler(state=CreateNews.title)
async def load_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await CreateNews.next()
    await message.reply("Введите описание")

@dp.message_handler(state=CreateNews.small_text)
async def load_descript(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['small_text'] = message.text
        print(1)
    await CreateNews.next()
    await message.reply("Добавте изоображение новости")

@dp.message_handler(content_types=['photo'],state=CreateNews.image)
async def load_image(message: types.Message, state: FSMContext):
    async with state.proxy() as data:

        file_info = await bot.get_file(message.photo[-1].file_id)
        file_path = file_info.file_path
        # my_object = await bot.download_file(file_path)

        my_io = io.BytesIO()

        file_id = message.photo[-1].file_id
        data["image_id"] = file_id
        await bot.download_file(file_path  = file_path, destination = my_io)

        binary_data = my_io.read()
        data_base64 = base64.b64encode(binary_data)
        
        base64_string = data_base64.decode('utf-8')
        data["image"] = base64_string
        

    await CreateNews.next()
    await message.reply("Введите содержание новости")

@dp.message_handler(state=CreateNews.text)
async def load_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        data['id'] = message.from_user.id 

    url = "http://myservices:7000/addNews"
    params = data.as_dict()
    resultGet = requests.post(url, params)   

    if resultGet.text == 'True':
        await message.reply("Новость успешно добавленна")
    else:
        await message.reply("Ошибка")
    await state.finish()








class Login(StatesGroup):
    username = State()
    password = State()

@dp.message_handler(commands=['start'], state=None)
async def command_start(message: types.Message):
    check_user_auth(message.from_user.id)
    if not userIsAut:
        await Login.username.set()
        await bot.send_message(message.from_user.id, "Введите имя пользователя:", reply_markup=mainMenu)
    else:
        await bot.send_message(message.from_user.id, "Вы уже авторезировались", reply_markup=secondMenu)


@dp.message_handler(state=Login.username)
async def load_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await Login.next()
    await message.reply("Введите пароль:")

@dp.message_handler(state=Login.password)
async def load_password(message: types.Message, state: FSMContext):
    global userIsAut
    async with state.proxy() as data:
        data['password'] = message.text
        data['id'] = message.from_user.id 

    url = "http://myservices:7000/TelegramPassword"
    params = data.as_dict()
    resultGet = requests.get(url, params)
    if resultGet.text == 'True':
        userIsAut = True
        await message.reply("Вы успешно авторезировались")

    else:
        await message.reply("Авторизация не прошла")
    await state.finish()

#Кнопки
btnStart = KeyboardButton('/start')
btnCreate = KeyboardButton('/create')
btnClose = KeyboardButton('/отмена')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStart, btnClose)
secondMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCreate, btnClose)
thirdMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnClose)
fourthMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStart, btnCreate,btnClose)


# Общая часть
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)