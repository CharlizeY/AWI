import sys
import requests
import bs4
from bs4 import BeautifulSoup

Req  = requests.get(sys.argv[1])
soup = BeautifulSoup(Req.content, 'lxml')
Div = soup.find('div', {'id' : 'infos'})

Artwork = {
    'Artist' : 'Unlisted',
    'Type' : 'Unlisted',
    'Title' : 'Unlisted',
    'Year' : 'Unlisted',
    'Category' : 'Unlisted',
    'Medium' : 'Unlisted',
    'Signature' : 'Unlisted',
    'Size' : 'Unlisted',
    'Certifate' : 'Unlisted',
    'Invoice' : 'Unlisted',
    'Condition' : 'Unlisted',
    'Ad' : 'Unlisted',
    'Price' : 'Unlisted'
}

def find(Div, Section):
    return Div.find_all('td', {'class' : Section})

for section, value in zip(find(Div, 'section'), find(Div, 'value')):
    # print(section.text, value.text)

    if ('Artist' in section.text):
        Artwork['Artist'] = value.text
    if ('Type' in section.text):
        Artwork['Type'] = value.text
    if ('Title' in section.text):
        Artwork['Title'] = value.text
    if ('Year' in section.text):
        Artwork['Year'] = value.text
    if ('Category' in section.text):
        Artwork['Category'] = value.text
    if ('Medium' in section.text):
        Artwork['Medium'] = value.text
    if ('Signature' in section.text):
        Artwork['Signature'] = value.text
    if ('Size' in section.text):
        Artwork['Size'] = value.text
    if ('Certifate' in section.text):
        Artwork['Certifate'] = value.text
    if ('Invoice' in section.text):
        Artwork['Invoice'] = value.text
    if ('Condition' in section.text):
        Artwork['Condition'] = value.text
    if ('Ad' in section.text):
        Artwork['Ad'] = value.text
    if ('Price' in section.text):
        Artwork['Price'] = value.text


print(Artwork)
