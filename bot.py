import telebot
import random
import requests
from datetime import datetime, timezone, timedelta
import weather_parser as parser


TOKEN = 'KEY'

bot = telebot.TeleBot(TOKEN)

def logger(name, username, text):
    time_now = datetime.now(timezone.utc).astimezone() + timedelta(hours=2)
    #file = open('log.txt', 'a', encoding='UTF-8')
    #file.write(f'name\tusername\ttext\t{str(time_now.strftime("%d:%m:%Y %H:%M:%S"))}\n')
    #file.close
    print(f'{name}\t{username}\t{text}\t{str(time_now.strftime("%d:%m:%Y %H:%M:%S"))}')
          
          
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     f'Привет, {str(message.from_user.first_name)} !!\nЯ умею шутить и предсказывать погоду. Основные команды: "шутка", "погода", "погода завтра".\nДля подробностей введите /help')
    logger(message.chat.first_name, message.chat.username, message.text)
          
          
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Доступные команды:\nшутка - случайный анекдот\nпогода - какая сегодня погода\nпогода завтра - прогноз погоды на завтра')
    logger(message.chat.first_name, message.chat.username, message.text)
          
          
@bot.message_handler()
def echo_all(message: telebot):
    text = str(message.text).lower()
    if 'шутка' in text:
        r = requests.get('http://rzhunemogu.ru/RandJSON.aspx?1')
        t = r.text
        bot.send_message(message.chat.id, str(t[12:-2]))
    elif 'погода' in text:
        bot.send_message(message.chat.id, f'Температура:{parser.get_today_temp(text)}\n\n{parser.day_description(text)}')
    elif 'погода завтра' in text:
        bot.send_message(message.chat.id, f'Температура:{parser.get_today_temp(text)}\n\n{parser.day_description(text)}')
    else:
        bot.reply_to(message, 'Такой команды нет.\n/help - список доступных команд')
          
    logger(message.chat.first_name, message.chat.username, message.text)

bot.polling(none_stop=True)
