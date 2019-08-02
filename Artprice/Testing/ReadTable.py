import requests
import sys
import bs4
from bs4 import BeautifulSoup

Req = requests.get(sys.argv[1])
soup = BeautifulSoup(Req.content, "lxml")
Div = soup.find("div", {"id" : "infos"})

def findRows(attribute, array):
    for tag in Div.find_all('td', attrs={'class': attribute}):
        array.append(tag.text)

Parameters = []
Values = []
findRows('section', Parameters)
findRows('value', Values)

index = 0
for param in Parameters:
    index = index + 1
    if("Size" in param):
        sizeIndex = index - 1
    if("Price" in param):
        priceIndex = index - 1
    if("Artist" in param):
        ArtistIndex = index - 1
    if("Title" in param):
        TitleIndex = index - 1
    else:
        continue

Artist = Values[ArtistIndex]
Title = Values[TitleIndex]

Dimensions = Values[sizeIndex]
DimSplit = Dimensions.splitlines()
for line in DimSplit:
    if ("in" in line):
        SizeInches = line
    elif ("cm" in line):
        SizeCM = line
    else:
        continue

Price = Values[priceIndex]
PriceSplit = Price.splitlines()
for line in PriceSplit:
    if ("$" in line):
        PriceDollars = line
    elif ("£" in line):
        PriceSterling = line
    else:
        continue

print(Artist)
print(Title)
print(SizeInches)
print(SizeCM)
print(PriceDollars)
print(PriceSterling)
