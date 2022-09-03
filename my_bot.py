from telebot import *
from my_config import TOKEN
from new_rarse_json import get_response, parse, my_url
import models
from models import Course, BaseModel, TGUser


from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,

)

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    text = f"""Здравствуйте! Здесь вы можете посмотреть все наши курсы ."""
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    continue_step = InlineKeyboardButton(f"Нажмите сюда чтобы посмотреть курсы ", callback_data="course_menu")
    markup.add(continue_step)
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == "course_menu")
def course_menu(callback: types.CallbackQuery):
    list_of_data = get_response(my_url)
    list_of_data = parse(my_url)
    Course.create_from_list(list_of_data)
    text = ''
    for data in list_of_data:
        text += data['title'] + '\n'

        print(f'{data}ewhr')
    print(f"jfgfH{text}")
    bot.send_message(callback.message.chat.id, text)


bot.infinity_polling()





