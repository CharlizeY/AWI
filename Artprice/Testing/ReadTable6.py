

def ExtractTableHTML(URL):

    import sys
    import requests
    import bs4
    from bs4 import BeautifulSoup

    Req  = requests.get(URL)
    soup = BeautifulSoup(Req.content, 'lxml')
    Div = soup.find('div', {'id' : 'infos'})

    Params = ['Arist', 'Type', 'Title', 'Year', 'Category', 'Medium', 'Signature', 'Size', 'Certifacte', 'Invoice', 'Condition', 'Ad', 'Price']
    Values = ['Unlisted'] * len(Params)
    Artwork = {}

    for param, value in zip(Params, Values):
        Artwork.update({param : value})

    def find(Div, Section):
        return Div.find_all('td', {'class' : Section})

    def match(Param, section, value, Artwork):
        if (Param in section.text):
            Artwork[Param] = value.text

    for section, value in zip(find(Div, 'section'), find(Div, 'value')):
        for Param in list(Artwork.keys()):
            match(Param, section, value, Artwork)

    return Artwork
