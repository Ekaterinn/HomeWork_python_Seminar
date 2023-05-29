import telebot
import requests

bot = telebot.TeleBot("")  

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	
@bot.message_handler(content_types=['text'])
def greetings(message):
    text = message.text
    if text == 'погода':
       req = requests.get('https://wttr.in/?0T')  
       bot.reply_to(message, req.text)
    elif text == 'кот':
       req = requests.get('https://cataas.com/cat')  
       bot.send_photo(message.from_user.id, req.content)
 

bot.polling()

# if 'привет' in text:
# 		bot.reply_to(message, f'Привет, {message.from_user.first_name}!')