# Imports
import csv
import telebot

from My_Universe.Correct_login.Future_me.set_future_message import add_new_message, add_new_message_date, save_message
from My_Universe.check_login import check_login
from My_Universe.sign_in import register
from telebot.types import BotCommand, ReplyKeyboardRemove
from environs import Env
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from My_Universe.Correct_login.correct_login import all_of_them
from My_Universe.Correct_login.Future_me.future_window import future_window_fun
from My_Universe.Correct_login.My_account.account_window import account_window_fun
from My_Universe.Correct_login.My_goals.goal_window import goal_window_fun


env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
simple_bot = telebot.TeleBot(BOT_TOKEN)

all_dict = {
    'id': "",
    "name": "",
    "password": ""
}


# Keyboard button
def key_button():
    login_or_sign = ReplyKeyboardMarkup(resize_keyboard=True)
    login_or_sign.add(KeyboardButton(f"Login✅"), KeyboardButton(f"Sign in✅"))
    return login_or_sign


# start
@simple_bot.message_handler(commands=["start"])
def start_message(message):
    name_f = message.from_user.first_name
    simple_bot.send_message(message.chat.id, f"Hi {name_f}👇", reply_markup=key_button())


# exit
@simple_bot.message_handler(commands=["exit"])
def exit_message(message):
    name_f = message.from_user.first_name
    simple_bot.send_message(message.chat.id, f"EXIT", reply_markup=key_button())


# Password know
@simple_bot.message_handler(chat_types=['text'])
def password_know(message):
    all_dict['password'] = message.text
    simple_bot.send_message(message.chat.id, f"{register(all_dict)}👍")
    simple_bot.send_message(message.chat.id, f"Login!")
    exit_message(message)


# name know
@simple_bot.message_handler(chat_types=['text'])
def name_know(message):
    all_dict['name'] = message.text
    all_dict['id'] = message.chat.id
    simple_bot.send_message(message.chat.id, f"Enter Password:")
    simple_bot.register_next_step_handler(message, password_know)


# Check login password
@simple_bot.message_handler(chat_types=['text'])
def check_lo(message):
    one_zero = check_login(message.chat.id, message.text)
    if one_zero == "exit":
        simple_bot.send_message(message.chat.id, f"You have not account!!!")
        exit_message(message)
    elif one_zero == "1":
        all_of_them(message)
    else:
        simple_bot.send_message(message.chat.id, f"{one_zero}")


time_now = {
    'time': "",
    'text': ""
}


# Date and text
@simple_bot.message_handler(chat_types=['text'])
def date_and_text(message):
    time_now['text'] = message.text[5:]
    save_message(message, f"{time_now.get('time')}", f'{time_now.get("text")}')


# Login or sign in
@simple_bot.message_handler(func=lambda message: True)
def login_sign_button(message):
    if message.text == "Login✅":
        simple_bot.send_message(message.chat.id, f"Password:")
        simple_bot.register_next_step_handler(message, check_lo)
    elif message.text[0:4] == 'date':
        with open("login.csv", "r+", newline="\n") as f:
            file_read = csv.DictReader(f)
            for i in file_read:
                if i['id'] == f"{message.chat.id}":
                    if add_new_message_date(message, message.text[5:]) == '1':
                        time_now['time'] = message.text[5:]
                        simple_bot.send_message(message.chat.id,
                                                f"Good {i['name']} enter text Example = text:")
                        simple_bot.register_next_step_handler(message, date_and_text)
    elif message.text == "Sign in✅":
        c = True
        with open("login.csv", "r+", newline="\n") as f:
            file_read = csv.DictReader(f)
            for i in file_read:
                if i['id'] == f"{message.chat.id}":
                    c = False
                    simple_bot.send_message(message.chat.id,
                                            f"{message.from_user.first_name} you have already account!!")
                    exit_message(message)
        if c:
            simple_bot.send_message(message.chat.id, f"What can i call you:")
            simple_bot.register_next_step_handler(message, name_know)
    elif message.text == "Future Message✍️":
        future_window_fun(message)
    elif message.text == "My goals🦾":
        goal_window_fun(message)
    elif message.text == "My account📄":
        account_window_fun(message)
    elif message.text == "Add future Message➕":
        add_new_message(message)
    elif message.text == "delete message🗑":
        pass
    elif message.text == "back 🔙":
        all_of_them(message)
    elif message.text == "back🔙":
        exit_message(message)


# Commands
def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/exit", "sign out")
    ]


if __name__ == '__main__':
    simple_bot.set_my_commands(my_commands())
    simple_bot.infinity_polling()
