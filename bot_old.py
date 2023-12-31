import os

import telebot
from telegram import (
    Update,
    User,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    BotCommand
)
from gpt import get_response

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    print('[user]', bot.get_my_name())
    # print('[chat]', bot.get_chat())
    # bot.reply_backend("hi")
    # bot.send_message("@akn_714", 'hi!')
    # update.message.chat.send_action(action="typing")
    bot.reply_to(message, 'generating response...')
    response = get_response(message.text)
    bot.reply_to(message, response['choices'][0]['message']['content'])
    bot.reply_to(message, response['choices'][0]['related_links'])
    # bot.reply_to(bot.get_me())
    # await bot.reply_to(message, await get_response(message))

# this function replies the same message if it doesn't match with above commands in previous function
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


