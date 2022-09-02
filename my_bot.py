from telebot import telebot, types
from my_config import TOKEN
from new_rarse_json import get_response, parse, parse_objects, my_url
import models
from models import Course


from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,

)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    text = """Здравствуйте! Здесь вы можете посмотреть все наши курсы ."""
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    continue_step = InlineKeyboardButton("Нажмите сюда чтобы посмотреть курсы ", callback_data="course_menu")
    markup.add(continue_step)
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == "course_menu")
def course_menu(callback: types.CallbackQuery):
    list_of_data = parse_objects
    Course.create_from_list(list_of_data)
    text = ''
    for data in list_of_data:
        text += data['title'] + '\n'

    bot.send_message(callback.message.chat.id, text)


bot.infinity_polling()

#
# @bot.callback_query_handler(func=lambda call: call.data == "course_menu")
# def course_menu(call):
#     text = "СПИСОК ВСЕХ НАШИХ КУРСОВ"
#     parsing = parse('https://coursive.id/api/v1/courses')
#     course_list = f'{text} \n {parsing} '
#     bot.send_message(call.message.chat.id, course_list)



