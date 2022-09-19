import smtplib
from email.message import EmailMessage

import os

import bs4
import requests

getPage = requests.get('https://www.sportselect.ro/produse?c=dunk')
getPage.raise_for_status()
menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
shoes = menu.select('.title')

the_one = 'dunk'
flength = len(the_one)
available = []
file_shoes = []

# Verificam daca exista fisierul unde stocam adidasii deja cautati
if os.path.exists('shoes_sportselect.txt'):
    with open('shoes_sportselect.txt') as fr:
        lines = fr.read().splitlines()
        file_shoes.extend(lines)

for shoe in shoes:
    # Verificam daca h2-ul contine 'dunk' si adidasul nu a fost cautat in trecut
    if 'dunk' in shoe.text.lower() and shoe.text not in file_shoes:
        available.append(shoe.text)

if available:
    msg = EmailMessage()
    msg.set_content(f"Perechi noi: {','.join(available)}\nhttps://www.sportselect.ro/produse?c=dunk")
    msg['From'] = 'sneakersbotro@gmail.com'
    msg['To'] = 'teo_tzt@yahoo.com'
    msg['Subject'] = 'New Dunks Activity Report'
    fromaddr = 'sneakersbotro@gmail.com'
    toaddrs = ['teo_tzt@yahoo.com']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('sneakersbotro@gmail.com', 'kuqbvomhdsglfmrq')
    server.send_message(msg)
    server.quit()
    # Scriem in fisier noile perechi
    with open('shoes_sportselect.txt', 'a') as fa:
        fa.write('\n'.join([s for s in available]))
        fa.write('\n')