"Добавьте в telegram-бота игру «Угадай числа»."
"Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов."

import telebot
import random

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message.chat.id, "Привет. Я хочу сыграть с тобой в игру. Я загадал число от 1 до 1000, попробуй угадать")

@bot.message_handler(content_types=['text'])
def greetings(message):
	rAndom = str(random.randint(1,1000))
	count = 1
	data = open('log.txt', mode='a', encoding='utf-8')
	text = f'{message.text}\n'
	data.write(text)
	data.close()
	if message.text == 	rAndom:
			bot.reply_to(f"Вы угадали. Количество попытток {count}")
	else:
		print("Вы не угадали. Введите новое число")
		while message.text != rAndom:
			if message.text == rAndom:
				bot.reply_to(f"Вы угадали. Количество попытток {count}")
		count += 1
bot.polling()