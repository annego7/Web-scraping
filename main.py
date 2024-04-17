import requests
from bs4 import BeautifulSoup
import time
import random

def scrape(url):
    odziv = requests.get(url)

    if odziv.status_code == 200:
        vsebina = BeautifulSoup(odziv.content, 'html.parser')
        oglasi = vsebina.find_all('li', {'class': 's-item'})
        n = 0

        with open('C:\\Users\\Asus\\Downloads\\seminarska\\scrape.txt', 'w', encoding='utf-8') as datoteka:

            for oglas in oglasi:

                naslov = oglas.find('div', {'class': 's-item__title'})
                if naslov:
                    naslov = naslov.text.strip()

                    if 'faulty' in naslov.lower():
                       continue

                    if 'unlocked' in naslov.lower():

                       cena1 = oglas.find('span', {'class': 's-item__price'})
                       if cena1:
                         cena = cena1.text.strip()
                         if 'to' in cena:
                           cena = cena.split('to')[0].strip()

                         cena_brez_valute = cena.replace('$', '').replace(',', '')
                         cena_stevilka = int(float(cena_brez_valute))

                         lokacija1 = oglas.find('span', {'class': 's-item__location'})
                         lokacija = lokacija1.text.strip() if lokacija1 else 'N/A'

                         povezava1 = oglas.find('a', {'class': 's-item__link'})
                         povezava = povezava1['href']

                         if cena_stevilka <= 200:
                            n += 1
                            datoteka.write('Naslov: ' + naslov + '\n')
                            datoteka.write('Cena: ' + cena + '\n')
                            datoteka.write('Lokacija: ' + lokacija.replace('from ', '') + '\n')
                            datoteka.write('Povezava: ' + povezava + '\n')
                            datoteka.write('-----------------------\n')
                            print('Uspešno najdeno ' + str(n) + ' ustreznih oglasov!') 
                     
                    time.sleep(random.uniform(1, 6)) 
    else:
        print('Napaka:', odziv.status_code)

scrape('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=iphone+11&_sacat=0&_odkw=marshal&_osacat=0')