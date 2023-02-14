# All
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import csv
import telebot
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
simple_bot = telebot.TeleBot(BOT_TOKEN)


@simple_bot.message_handler(chat_types=['text'])
def all_of_them(message):
    name_call = ""
    with open("login.csv", "r+") as read:
        file_read = csv.DictReader(read)
        for i in file_read:
            if i['id'] == f"{message.chat.id}":
                name_call = i['name']

    # Keyboard button
    def key_button():
        login_or_sign = ReplyKeyboardMarkup(resize_keyboard=True)
        login_or_sign.add(KeyboardButton(f"Future Message✍️"), KeyboardButton(f"My goals🦾"),
                          KeyboardButton("My account📄"), KeyboardButton("back🔙"))
        return login_or_sign

    simple_bot.send_message(message.chat.id, f"Welcome {name_call} to your UNIVERSE 🪐 👇",
                            reply_markup=key_button())


if __name__ == '__main__':
    simple_bot.infinity_polling()
