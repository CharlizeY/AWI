import config
import bs4
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser

br = RoboBrowser(parser='html.parser', history = True)
br.open('https://www.artprice.com/identity')
form = br.get_form()
form['login'] = config.DATACOUP_USERNAME
form['pass'] = config.DATACOUP_PASSWORD
br.submit_form(form)

soup = br.parsed
info = soup.find_all('script')
accountInfo = info[len(info)-1]
strInfo = str(accountInfo)
index = strInfo.find('idcustomer')

i = 0
id = []
while(True):
    i = i + 1
    try:
        id.append(int(strInfo[index + i]))
    except:
        continue
    if(len(id) == 9):
        break

for i in range(0, len(id)):
    id[i] = str(id[i])
user = ''.join(id)
print('User number = ', user)
