# All
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import BotCommand
import json
import csv
import telebot
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
simple_bot = telebot.TeleBot(BOT_TOKEN)


# future window
@simple_bot.message_handler(chat_types=['text'])
def account_window_fun(message):
    name_call = ""
    with open("login.csv", "r+") as read:
        file_read = csv.DictReader(read)
        for i in file_read:
            if i['id'] == f"{message.chat.id}":
                name_call = i['name']

    #  Future Keyboard button
    def key_button():
        login_or_sign = ReplyKeyboardMarkup(resize_keyboard=True)
        login_or_sign.add(KeyboardButton(f"See account information👁"),
                          KeyboardButton("edit information✍️"), KeyboardButton("back 🔙"))
        return login_or_sign

    simple_bot.send_message(message.chat.id, f" Welcome your account 👩‍💻",
                            reply_markup=key_button())


if __name__ == '__main__':
    simple_bot.infinity_polling()
