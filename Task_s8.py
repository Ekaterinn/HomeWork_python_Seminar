import telebot
import requests
import time

bot = telebot.TeleBot("6207493106:AAHOIXqwXhnG0b7-tEHfWAKx-EM351arHEU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def text_message(message):
	#print(message)
	data = open('fileBot.txt', mode='a', encoding='utf-8')
	text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
	data.write(text)
	data.close()
	if message.text == 'Хочу есть':
		data = open('IdRegistration.txt', mode='r', encoding='utf-8')
		id_list = data.readlines()
		data.close()
		id_list = list(el[:-1] for el in id_list)
		if str(message.from_user.id) not in id_list:
			data = open('IdRegistration.txt', mode='a', encoding='utf-8')
			data.write(f'{message.from_user.id}\n')
			data.close()
			bot.reply_to(message, 'Поиск ближайшего кафе на карте')
		else:
			bot.reply_to(message, 'Вы уже спрашивали')
	else:
		bot.reply_to(message, 'Что нужно от Бота?')
		
	
bot.polling()