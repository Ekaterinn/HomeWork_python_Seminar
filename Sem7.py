import telebot
import requests

bot = telebot.TeleBot("6207493106:AAHOIXqwXhnG0b7-tEHfWAKx-EM351arHEU")  #, parse_mode=None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
	
@bot.message_handler(content_types=['text'])
def greetings(message):
	# print(message)
	text = message.text
	# if 'привет' in text:
	# 	bot.reply_to(message, f'Привет, {message.from_user.first_name}!')
    if text == 'погода':
        req = requests.get('https://wttr.in/?0T')  
        bot.reply_to(message, req.text)



bot.polling()