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
indices = []

findRows('section', Parameters)
findRows('value', Values)

def FindParameter(Parameter, Array):
    for line in Array:
        if(Parameter in line):
            Output = line
            indices.append(Array.index(line))
        else:
            continue
    try:
        return Output
    except:
        return False

Artist = FindParameter('Artist', Parameters)
Title = FindParameter('Title', Parameters)
Size = FindParameter('Size', Parameters)
Price = FindParameter('Price', Parameters)




class Artwork:
    Artist = 'Artist'
    Price = 'Price'

Names = ['Bob', 'James', 'Helen', 'Sam', 'Jess', 'Maria', 'Kat']
Price = 7 * ['£100']

def Assign(Artwork, Parameter):
    for param in Parameter:
        Artwork.Parameter = param
        print(Artwork.Parameter)

Assign(Artwork, Names)
Assign(Artwork, Price)
