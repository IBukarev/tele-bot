from bs4 import BeautifulSoup
import requests
import random


oven = 'https://horo.mail.ru/prediction/aries/today/'

r = requests.get(oven)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

oven_gor = []

for i in ank:
    oven_gor.append(i.getText())


telec = 'https://horo.mail.ru/prediction/taurus/today/'

r = requests.get(telec)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

telec_gor = []

for i in ank:
    telec_gor.append(i.getText())


bliznec = 'https://horo.mail.ru/prediction/gemini/today/'

r = requests.get(bliznec)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

bliznec_gor = []

for i in ank:
    bliznec_gor.append(i.getText())



raq = 'https://horo.mail.ru/prediction/cancer/today/'

r = requests.get(raq)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

raq_gor = []

for i in ank:
    raq_gor.append(i.getText())



lew = 'https://horo.mail.ru/prediction/leo/today/'

r = requests.get(lew)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

lew_gor = []

for i in ank:
    lew_gor.append(i.getText())




dev = 'https://horo.mail.ru/prediction/virgo/today/'

r = requests.get(dev)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

dev_gor = []

for i in ank:
    dev_gor.append(i.getText())




vesi = 'https://horo.mail.ru/prediction/libra/today/'

r = requests.get(vesi)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

vesi_gor = []

for i in ank:
    vesi_gor.append(i.getText())



skorp = 'https://horo.mail.ru/prediction/scorpio/today/'

r = requests.get(skorp)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

skorp_gor = []

for i in ank:
    skorp_gor.append(i.getText())


strel = 'https://horo.mail.ru/prediction/sagittarius/today/'

r = requests.get(strel)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

strel_gor = []

for i in ank:
    strel_gor.append(i.getText())


kozer = 'https://horo.mail.ru/prediction/capricorn/today/'

r = requests.get(kozer)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

kozer_gor = []

for i in ank:
    kozer_gor.append(i.getText())




vodol = 'https://horo.mail.ru/prediction/taurus/today/'

r = requests.get(vodol)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

vodol_gor = []

for i in ank:
    vodol_gor.append(i.getText())



fish = 'https://horo.mail.ru/prediction/pisces/today/'

r = requests.get(fish)

soup = BeautifulSoup(r.text, 'html.parser')

ank = soup.find(class_='article__item article__item_alignment_left article__item_html').find('p')

fish_gor = []

for i in ank:
    fish_gor.append(i.getText())


anekdot = 'https://nekdo.ru/'

r = requests.get(anekdot)
soup = BeautifulSoup(r.text, 'html.parser')
ank = soup.find_all('div', class_= 'text')

anekdot_list = []

for i in ank:
    anekdot_list.append(i.getText())


valuti = 'https://www.nbrb.by/statistics/rates/ratesdaily.asp'

valuta = []

r = requests.get(valuti)
soup = BeautifulSoup(r.text, 'html.parser')
ank = soup.find(class_='currencyTable').find('tbody').find_all('tr')

for i in ank:
    valut_n = i.find_all('td')

    nominal = valut_n[2].find('div').text

    valuta.append(nominal)

usd = []
eur = []
rub = []
uah = []

usd.append(valuta[7])
eur.append(valuta[9])
rub.append(valuta[21])
uah.append(valuta[4])