import telebot
import pars
from telebot import types
import random


bot = telebot.TeleBot('5464898728:AAHmtBpj14OUipMe2xZjnL62qfP3reMRNm8')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет {message.from_user.first_name} {message.from_user.last_name}, что бы узнать что я умею введи /help'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['help'])
def help(message):
    mess = 'Тут писаны команды которые я умею:\n /horoscope - узнать свой гороскоп\n /anecdot - Расскажу тебе анекдот(разные)' \
           '\n /random - Сгенерирую рандомное число от 1 до 100'
    bot.send_message(message.chat.id, mess)



@bot.message_handler(commands=['horoscope'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    oven = types.InlineKeyboardButton(text='Овен', callback_data='oven')
    telec = types.InlineKeyboardButton(text='Телец', callback_data='telec')
    bliznec = types.InlineKeyboardButton(text='Близнецы', callback_data='bliznec')
    raq = types.InlineKeyboardButton(text='Рак', callback_data='raq')
    lew = types.InlineKeyboardButton(text='Лев', callback_data='lew')
    dev = types.InlineKeyboardButton(text='Дева', callback_data='dev')
    vesi = types.InlineKeyboardButton(text='Весы', callback_data='vesi')
    skorp = types.InlineKeyboardButton(text='Скорпион', callback_data='skorp')
    strel = types.InlineKeyboardButton(text='Стрелец', callback_data='strel')
    kozer = types.InlineKeyboardButton(text='Козерог', callback_data='kozer')
    vodol = types.InlineKeyboardButton(text='Водолей', callback_data='vodol')
    fish = types.InlineKeyboardButton(text='Рыбы', callback_data='fish')
    markup.add(oven,telec,bliznec,raq,lew,dev,vesi,skorp,strel,kozer,vodol,fish)
    mess = f'Привет {message.from_user.first_name} {message.from_user.last_name}, я бот, который расскажет тебе твой гороскоп на сегодня! Кто ты по гороскопу?'
    bot.send_message(message.chat.id, mess, reply_markup=markup)

@bot.message_handler(commands=['curs'])
def exchange(message):
    markups = types.InlineKeyboardMarkup()
    dollar = types.InlineKeyboardButton(text='Доллар', callback_data='dollar')
    euro = types.InlineKeyboardButton(text='Евро', callback_data='euro')
    rub = types.InlineKeyboardButton(text='Российский рубль', callback_data='rub')
    uah = types.InlineKeyboardButton(text='Украинская гривна', callback_data='uah')
    markups.add(dollar,euro,rub,uah)
    mess = f'Я покажу тебе курс валют на сегодняшний день, какая валюта тебя интересует?'
    bot.send_message(message.chat.id, mess, reply_markup=markups)

@bot.callback_query_handler(func = lambda call: True)
def call_back_inline(call):
    if call.data == 'oven':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для овна: {pars.oven_gor}')
    elif call.data == 'telec':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для тельца: {pars.telec_gor}')
    elif call.data == 'bliznec':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для близнецов: {pars.bliznec_gor}')
    elif call.data == 'raq':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для рака: {pars.raq_gor}')
    elif call.data == 'lew':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для льва: {pars.lew_gor}')
    elif call.data == 'dev':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для девы: {pars.dev_gor}')
    elif call.data == 'vesi':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для весов: {pars.vesi_gor}')
    elif call.data == 'skorp':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для скорпиона: {pars.skorp_gor}')
    elif call.data == 'strel':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для стрельца: {pars.strel_gor}')
    elif call.data == 'kozer':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для козерога: {pars.kozer_gor}')
    elif call.data == 'vodol':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для водолея: {pars.vodol_gor}')
    elif call.data == 'fish':
        bot.send_message(call.message.chat.id, f'Вот гороскоп для рыб: {pars.fish_gor}')




@bot.message_handler(commands=['anecdot'])
def anecdot(message):
    anec = f'Как тебе такой анекдот: {random.choice(pars.anekdot_list)}'
    bot.send_message(message.chat.id, anec)


@bot.message_handler(commands=['random'])
def randoom(message):
    bot.send_message(message.chat.id, f'{random.randint(1,100)}')


@bot.callback_query_handler(func = lambda call: True)
def exchange_inline(call):
    if call.data == 'dollar':
        bot.send_message(call.message.chat.id, f'Вот курс доллара к бел.рублю на сегодняшний день: {pars.usd}')
    elif call.data == 'euro':
        bot.send_message(call.message.chat.id, f'Вот курс евро к бел.рублю на сегодняшний день: {pars.eur}')
    elif call.data == 'rub':
        bot.send_message(call.message.chat.id, f'Вот курс российского рубля к бел.рублю на сегодняшний день: {pars.rub}')
    elif call.data == 'uah':
        bot.send_message(call.message.chat.id, f'Вот курс украинской гривны к бел.рублю на сегодняшний день: {pars.uah}')


bot.polling(non_stop= True)