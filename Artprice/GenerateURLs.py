import webbrowser
import requests
import csv
import bs4
from bs4 import BeautifulSoup
from FindMaxPage import MaxPage
import pandas as pd

ArtPriceURL = 'https://www.artprice.com/marketplace'
MaxPageNum = MaxPage(ArtPriceURL)
print(MaxPageNum)

str1 = 'https://www.artprice.com/marketplace?idcurrencyzone=2&p='
str2 = '&sort=sort_dt-desc'

#Opens the last page in the list
urlMax = str1 + str(MaxPageNum) + str2
webbrowser.open(urlMax)

Links = []
for i in range(1, MaxPageNum):
    print('Page :', i)
    url = str1 + str(i) + str2
    Req = requests.get(url)
    soup = BeautifulSoup(Req.content, "lxml")
    Div = soup.find_all("div", {"class": "img"})

    for link in Div:
        link = link.find('a')['href']
        link = 'https://www.artprice.com' + link
        Links.append(link)
        print(link)

# ExtractedURLs = open("ExtractedURLs.csv",'w')
# wr = csv.writer(ExtractedURLs, dialect='excel')
# for link in Links:
#     wr.writerow([link])
