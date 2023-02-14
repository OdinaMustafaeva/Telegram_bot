import json
import datetime
import csv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
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
def add_new_message(message):
    simple_bot.send_message(message.chat.id,
                            f"{know_name_call(message)} enter your future message date time Example = date:{datetime.datetime.today().strftime('%Y-%m-%d')}")


@simple_bot.message_handler(chat_types=['text'])
def add_new_message_date(message, text):
    try:
        time = datetime.datetime.fromisoformat(f'{text}').strftime('%Y-%m-%d')
    except Exception:
        simple_bot.send_message(message.chat.id,
                                f"Something is wrong in time!")
    else:
        simple_bot.send_message(message.chat.id,
                                f"{time}")
        return '1'


@simple_bot.message_handler(chat_types=['text'])
def save_message(message, datee, real_text):
    with open(f"{message.chat.id}.json", "r+", newline="\n") as json_file_read:
        with open(f"{message.chat.id}.json", "a+", newline="\n") as json_file_write:
            for_file = {
                f"{datee}": {
                    'text': f"{real_text}"
                }
            }
            read = json.load(json_file_read)
            my_new_mesage = read["future_m"]
            read["future_m"] = for_file
            json_file_write.write(json.dumps(read))


if __name__ == '__main__':
    simple_bot.infinity_polling()
