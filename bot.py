import telebot
import random
import requests
from datetime import datetime, timezone, timedelta
import weather_parser as parser


TOKEN = '1101438623:AAFZInJNcB7A6S95VREDzg1z5S8XAs900cw'

bot = telebot.TeleBot(TOKEN)

def logger(name, username, text):
    time_now = datetime.now(timezone.utc).astimezone() + timedelta(hours=2)
    #file = open('log.txt', 'a', encoding='UTF-8')
    #file.write(f'name\tusername\ttext\t{str(time_now.strftime("%d:%m:%Y %H:%M:%S"))}\n')
    #file.close
    print(f'name\tusername\ttext\t{str(time_now.strftime("%d:%m:%Y %H:%M:%S"))}\n')
          
          
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     f'Привет, {str(message.from_user.first_name)} !!\nЯ умею шутить и предсказывать погоду. Основные команды: "шутка", "погода", "погода завтра".\nДля подробностей введите /help')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Доступные команды:\nшутка - случайный анекдот\nпогода - какая сегодня погода\nпогода завтра - прогноз погоды на завтра')

@bot.message_handler()
def echo_all(message: telebot):
    first_name = message.chat.first_name
    username = message.chat.username
    text = message.text
    if 'шутка' in message.text:
        r = requests.get('http://rzhunemogu.ru/RandJSON.aspx?1')
        t = r.text
        bot.send_message(message.chat.id, str(t[12:-2]))
    elif 'погода' in message.text:
        bot.send_message(message.chat.id, f'Температура:{parser.get_today_temp(message.text)}\n\n{parser.day_description(message.text)}')
    elif 'погода завтра'in message.text:
        bot.send_message(message.chat.id, f'Температура:{parser.get_today_temp(message.text)}\n\n{parser.day_description(message.text)}')

    logger(first_name, username, text)

bot.polling(none_stop=True)
