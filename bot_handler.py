import constants
from telebot import *
from databases.handling import *

TOCKEN = constants.TOKEN

bot = TeleBot(TOCKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.from_user.id, "У тебя уже есть учетная запись?")
    bot.send_message(message.from_user.id, "Если да, то напиши /signin. Если нет то зарегистрируйся по команде /register")


@bot.message_handler(commands=["register"])
def register(message):
    pass


def get_name(message):
    pass


def get_password(message):
    pass


def confirm(message):
    pass


bot.polling(none_stop=True, interval=0)
