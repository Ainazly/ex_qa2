from telebot import telebot, types
from my_config import TOKEN
from new_rarse_json import get_response, parse, parse_objects
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


@bot.callback_query_handler(func=lambda call: call.data == "course_menu")
def course_menu(call):
    text = "СПИСОК ВСЕХ НАШИХ КУРСОВ"
    parsing = parse('https://coursive.id/api/v1/courses')
    course_list = f'{text} \n {parsing} '
    bot.send_message(call.message.chat.id, course_list)


bot.infinity_polling()

