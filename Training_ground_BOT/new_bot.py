# Задание 1 необязательное Сделайте локальный чат-бот с внешним хранилищем. 
# Тема чат-бота - любая вам интересная.
import os
os.system('cls')
import telebot
from random import *
import json
import requests




games = []
API_URL = 'https://7012.deeppavlov.ai/model'
API_TOKEN = '6300491321:AAG5GZLVRTepCSNFDvlNJZO0vRAianfSzx4'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    games.append('Final  Fantasy')
    games.append('Legends of Heroes')
    games.append('Front Mission')
    games.append('Chrono Cross')
    games.append('Dragon Quest')
    bot.send_message(message.chat.id, 'Игры были загружены по умолчанию!')

@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id, 'Вот список игр: ')
        bot.send_message(message.chat.id, ', '.join(games))
    except:
        bot.send_message(message.chat.id, 'Игр нет ТТ')

@bot.message_handler(commands=['save'])
def save_all(message):
    with open('games.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(games,ensure_ascii=False))
    bot.send_message(message.chat.id, 'Игротека сохранена в файле games.json')

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = ' '.join(quest)
    data = {'question_raw': [qq]}
    try:
        res = requests.post(API_URL, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, 'что-то пошло не так')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if 'дела' in message.text.lower():
        bot.send_message(message.chat.id, 'Дела норм, ты как сам?')


bot.polling()  # bot start (while true)