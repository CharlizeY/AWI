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

# ParamOut = [Artist, Title, Size, Price]
# print(ParamOut)
#
# for index in indices:
#     print(Values[index])
#
# for Param in ParamOut:
#     if(Param == False):
#         print('Unlisted')
#     else:
#         continue

RequestedValues = []
for index in indices:
    RequestedValues.append(Values[index])

print(RequestedValues)
