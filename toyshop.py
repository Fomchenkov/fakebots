#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

Send to bot this message
1.	/start
2.	/category
3.	Lego Star Wars

"""


import telebot
from telebot import types


BOT_TOKEN = '387480715:AAGE4QwIkF6OaTaCln8vB4eAWPwD8Nes_fM'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
	text = "Я бот магазина игрушек. Тут вы можете выбрать игрушку для своего ребенка! "
	text += "Отправьте команду /category что бы посмотреть категории игрушек."
	return bot.send_message(message.chat.id, text, parse_mode="markdown")


@bot.message_handler(commands=['category'])
def cmd_start(message):
	keyboard = types.InlineKeyboardMarkup()
	c1 = types.InlineKeyboardButton(text="Lego", callback_data="c1")
	c2 = types.InlineKeyboardButton(text="Мягкие игрушки", callback_data="c2")
	c3 = types.InlineKeyboardButton(text="Развивающие игры", callback_data="c3")
	c4 = types.InlineKeyboardButton(text="Настольные игры", callback_data="c4")
	keyboard.add(c1)
	keyboard.add(c2)
	keyboard.add(c3)
	keyboard.add(c4)
	text = "Пожалуйста, выберите катeгорию."
	return bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	text = "Выбрана категория *Lego*\nВыберите подкатегорию"
	keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
	c1 = types.KeyboardButton(text="Lego Star Wars")
	c2 = types.KeyboardButton(text="Lego Friends")
	c3 = types.KeyboardButton(text="Lego Angry Birds")
	c4 = types.KeyboardButton(text="Lego BrickHeadz")
	c5 = types.KeyboardButton(text="Lego City")
	keyboard.add(c1)
	keyboard.add(c2)
	keyboard.add(c3)
	keyboard.add(c4)
	keyboard.add(c5)
	bot.send_message(call.message.chat.id, text, parse_mode="markdown", reply_markup=keyboard)


@bot.message_handler(func=lambda arg: True)
def text_handler(message):
	text = "*Lego Star Wars* - отличный выбор! Вот один из наших популярных наборов."
	bot.send_message(message.chat.id, text, parse_mode="markdown")

	text = "Набор LEGO Star Wars Конструктор Стрела 75186"
	photo_url = "http://lego.brickinstructions.com/75000/75174/001.jpg"
	bot.send_photo(message.chat.id, photo_url, caption=text)


if __name__ == '__main__':
	bot.polling(none_stop=True)
