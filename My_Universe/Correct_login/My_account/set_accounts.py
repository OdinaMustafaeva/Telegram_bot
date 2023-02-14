import json
import datetime
import csv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOaKEN")
simple_bot = telebot.TeleBot(BOT_TOKEN)


def know_name_call(message):
    name_call = ""
    with open("login.csv", "r+") as read:
        file_read = csv.DictReader(read)
        for i in file_read:
            if i['id'] == f"{message.chat.id}":
                name_call = i['name']
    return name_call


@simple_bot.message_handler(chat_types=['text'])
def see_information(message):
    pass


@simple_bot.message_handler(chat_types=['text'])
def edit_information(message, text):
    pass


if __name__ == '__main__':
    simple_bot.infinity_polling()
