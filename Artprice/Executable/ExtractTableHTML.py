def ExtractTableHTML(URL):
    import re
    import sys
    import requests
    import unicodedata
    import bs4
    from bs4 import BeautifulSoup

    Req  = requests.get(URL)
    soup = BeautifulSoup(Req.content, 'lxml')
    Div = soup.find('div', {'id' : 'infos'})

    Params = ['Artist', 'Type', 'Title', 'Year', 'Category', 'Medium', 'Signature', 'Size', 'Certificate', 'Invoice', 'Condition', 'Ad', 'Price']
    Values = ['Unlisted'] * len(Params)
    Artwork = {}

    for param, value in zip(Params, Values):
        Artwork.update({param : value})

    def find(Div, Section):
        return Div.find_all('td', {'class' : Section})

    def match(Param, section, value, Artwork):
        if (Param in section.text):
            Artwork[Param] = value.text.rstrip().lstrip()
            if(Param == 'Artist'):
                Artwork[Param] = re.search('prices of (.*?)\n', Artwork[Param]).group(1)
            Artwork[Param] = str(unicodedata.normalize('NFD', Artwork[Param]).encode('ASCII', 'ignore'))
            Artwork[Param] = Artwork[Param][2:-1].replace('\\n', '')

    for section, value in zip(find(Div, 'section'), find(Div, 'value')):
        for Param in list(Artwork.keys()):
            match(Param, section, value, Artwork)

    return Artwork
