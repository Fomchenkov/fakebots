#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

Send to bot this messages
1.	/start
2.	/requests

"""


import telebot
from telebot import types


BOT_TOKEN = '387480715:AAGE4QwIkF6OaTaCln8vB4eAWPwD8Nes_fM'
bot = telebot.TeleBot(BOT_TOKEN)


users = {}

questions = [
	"Теперь укажите возраст вашего ребенка.",
	"Введите контактный номер телефона",
	"Напишите ваши рекомендации.",
	"Заявка заполнена! Мы свяжемся с вами для уточнения деталей."
]


@bot.message_handler(commands=['start'])
def cmd_start(message):
	text = "Я бот школы английского. Тут вы можете оставить заявку на обучение своего ребенка! "
	text += "Отправьте команду /request что бы начать."
	return bot.send_message(message.chat.id, text, parse_mode="markdown")


@bot.message_handler(commands=['request'])
def cmd_start(message):
	keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
	c1 = types.KeyboardButton(text="Подготовка к школе детей 5 и 6 лет")
	c2 = types.KeyboardButton(text="Школа современного английского языка")
	c3 = types.KeyboardButton(text="Центр раннего развития и школа творчества")
	keyboard.add(c1)
	keyboard.add(c2)
	keyboard.add(c3)
	text = "Пожалуйста, выберите направление."
	return bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(func=lambda arg: True)
def text_handler(message):
	if str(message.from_user.id) not in users:
		users[str(message.from_user.id)] = 0
	try:
		text = questions[users[str(message.from_user.id)]]
	except IndexError as e:
		text = questions[users[str(message.from_user.id)] - 1]
		return bot.send_message(message.chat.id, text)
	users[str(message.from_user.id)] += 1
	return bot.send_message(message.chat.id, text)


if __name__ == '__main__':
	bot.polling(none_stop=True)
