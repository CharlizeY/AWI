import requests
import bs4
from bs4 import BeautifulSoup

def MaxPage(ArtPriceURL):
    Req = requests.get(ArtPriceURL)
    soup = BeautifulSoup(Req.content, "lxml")
    Div = soup.find("div", {"data-react-class": "common/GoToPage"})

    Array = []
    Div = str(Div)
    for i in Div:
        try:
            Array.append(int(i))
        except:
            continue

    s = [str(i) for i in Array]
    res = int("".join(s))
    return res
