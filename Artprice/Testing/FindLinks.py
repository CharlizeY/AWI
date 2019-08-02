import requests
import bs4
from bs4 import BeautifulSoup

Req = requests.get('https://www.artprice.com/marketplace?idcurrencyzone=2&p=1751&sort=sort_dt-desc')
soup = BeautifulSoup(Req.content, "lxml")
Div = soup.find_all("div", {"class": "img"})

Links = []
for link in Div:
    link = link.find('a')['href']
    link = 'https://www.artprice.com' + link
    Links.append(link)

for link in Links:
    print(link, '\n')
