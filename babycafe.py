#!/usr/bin/python3
# -*- coding: utf-8 -*-


import telebot
from telebot import types


BOT_TOKEN = '387480715:AAGE4QwIkF6OaTaCln8vB4eAWPwD8Nes_fM'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
	text = "Я бот детской кафешки. Давайте закажем вкусный торт вашему ребенку! "
	text += "Отправьте команду /cakes что бы выбрать торт."
	return bot.send_message(message.chat.id, text, parse_mode="markdown")


@bot.message_handler(commands=['cakes'])
def cmd_start(message):
	keyboard = types.InlineKeyboardMarkup()
	c1 = types.InlineKeyboardButton(text="Наполеон", callback_data="c1")
	c2 = types.InlineKeyboardButton(text="Киевский торт", callback_data="c2")
	c3 = types.InlineKeyboardButton(text="Пражский торт", callback_data="c3")
	c4 = types.InlineKeyboardButton(text="Эстерхази", callback_data="c4")
	keyboard.add(c1)
	keyboard.add(c2)
	keyboard.add(c3)
	keyboard.add(c4)
	text = "Вот на выбор некоторые из наших тортов 🍰. Нажмите на копку, что бы посмотреть фотографию 🎂"
	return bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	text = "Выбран торт *Наполеон*"
	phoro_url = "https://takprosto.cc/wp-content/uploads/t/torty-praga-napoleon-i-medovik/1.jpg"
	bot.send_message(call.message.chat.id, text, parse_mode="markdown")
	bot.send_photo(call.message.chat.id, phoro_url)


if __name__ == '__main__':
	bot.polling(none_stop=True)
