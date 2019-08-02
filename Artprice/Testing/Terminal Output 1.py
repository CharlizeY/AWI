Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'urllib2'
>>> html = urllib.open("https://www.artprice.com/marketplace/1885025/georges-bastia/drawing-watercolor/luis-mariano-rossignol")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'urllib' has no attribute 'open'
>>> import urllib
>>> html = urllib.request.urlopen("https://www.artprice.com/marketplace/1885025/georges-bastia/drawing-watercolor/luis-mariano-rossignol")
>>> html
<http.client.HTTPResponse object at 0x11334c3c8>
>>> soup = BeautifulSoup(html)
/Users/JoyCowper/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <stdin>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "lxml")

  markup_type=markup_type))
>>> soup = BeautifulSoup(html, "lxml")
>>> soup

>>> soup

>>> for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
...     print link.get('href')
  File "<stdin>", line 2
    print link.get('href')
             ^
SyntaxError: invalid syntax
>>>
>>> for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
...     print(link.get('href'))
...
>>>
>>>
>>> html
<http.client.HTTPResponse object at 0x11334c3c8>
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
Joys-MacBook-Pro:~ JoyCowper$ tree
-bash: tree: command not found
Joys-MacBook-Pro:~ JoyCowper$ help tre
-bash: help: no help topics match `tre'.  Try `help help' or `man -k tre' or `info tre'.
Joys-MacBook-Pro:~ JoyCowper$ help tree
-bash: help: no help topics match `tree'.  Try `help help' or `man -k tree' or `info tree'.
Joys-MacBook-Pro:~ JoyCowper$ info tree
Joys-MacBook-Pro:~ JoyCowper$ clear

Joys-MacBook-Pro:~ JoyCowper$ python
Python 3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> import bs4
>>> from bs4 import BeautifulSoup
>>> import urllib
>>> request = requests.get("https://www.artprice.com/marketplace/1943107/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f")
>>> request
<Response [200]>
>>> request.history
[]
>>> delete request
  File "<stdin>", line 1
    delete request
                 ^
SyntaxError: invalid syntax
>>> request = 0
>>> request
0
>>> request = requests.get("https://www.artprice.com/marketplace/1500396/johann-heinrich-bleuler/drawing-watercolor/aussicht-von-vevey-uber-den-genfer-see")
>>> request
<Response [200]>
>>> request.history
[<Response [301]>, <Response [302]>]
>>> type(request)
<class 'requests.models.Response'>
>>> request(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Response' object is not callable
>>> request[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Response' object does not support indexing
>>> requests > 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'module' and 'int'
>>> try
  File "<stdin>", line 1
    try
      ^
SyntaxError: invalid syntax
>>> Try requests > 0
  File "<stdin>", line 1
    Try requests > 0
               ^
SyntaxError: invalid syntax
>>> Try request > 0
  File "<stdin>", line 1
    Try request > 0
              ^
SyntaxError: invalid syntax
>>> try:
...     request > 0
...
  File "<stdin>", line 3

    ^
SyntaxError: invalid syntax
>>> try:
...     request > 0
... except:
...     print("Error occured")
...
Error occured
>>> r1 = requests.get("https://www.artprice.com/marketplace/1597197/erich-buttner/drawing-watercolor/der-wachter")
>>> r1
<Response [200]>
>>> type(r1)
<class 'requests.models.Response'>
>>> type(request)
<class 'requests.models.Response'>
>>> str1 = str(r1)
>>> str1
'<Response [200]>'
>>> length(r1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'length' is not defined
>>> len(r1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'Response' has no len()
>>> for i in str1
  File "<stdin>", line 1
    for i in str1
                ^
SyntaxError: invalid syntax
>>> for i in str1:
...     print i
  File "<stdin>", line 2
    print i
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in str1:
...     print(i)
...
<
R
e
s
p
o
n
s
e

[
2
0
0
]
>
>>> for i in str1
  File "<stdin>", line 1
    for i in str1
                ^
SyntaxError: invalid syntax
>>> for i in str1:
...     num[i] = int(i)
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: '<'
>>> num
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'num' is not defined
>>> for i in str1:
...     if int(i) == True
  File "<stdin>", line 2
    if int(i) == True
                    ^
SyntaxError: invalid syntax
>>> for i in str1:
...     if int(i) == True:
...             print(i)
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: '<'
>>> x = '5'
>>> x
'5'
>>> int(x)
5
>>> r1
<Response [200]>
>>> str1
'<Response [200]>'
>>> for i in str1:
...     print(i)
...
<
R
e
s
p
o
n
s
e

[
2
0
0
]
>
>>> for i in str1:
...     if int(i) == True:
...             print('Yes!')
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: '<'
>>> int(<0
  File "<stdin>", line 1
    int(<0
        ^
SyntaxError: invalid syntax
>>> int(<)
  File "<stdin>", line 1
    int(<)
        ^
SyntaxError: invalid syntax
>>> try:
...     int('<')
...
  File "<stdin>", line 3

    ^
SyntaxError: invalid syntax
>>>
>>> try:
...     int('<')
... except:
...     print('error')
...
error
>>> try:
...     int(5)
... except:
...     print('error')
...
5
>>> for i in str1:
...     try:
...             int(i)
...     except:
...             print('error')
...
error
error
error
error
error
error
error
error
error
error
error
2
0
0
error
error
>>> for i in str1:
...     try:
...             int(i)
...     except:
...             continue
...
2
0
0
>>> i
'>'
>>> i
'>'
>>> i(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> i[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> request
<Response [200]>
>>> r1
<Response [200]>
>>> request
<Response [200]>
>>> request = requests.get("https://www.artprice.com/marketplace/1500396/johann-heinrich-bleuler/drawing-watercolor/aussicht-von-vevey-uber-den-genfer-see")
>>> request
<Response [200]>
>>> r2 = requests.get("https://www.artprice.com/marketplace/960643/christian-arrom/drawing-watercolor/personnages-ii")
>>> r2
<Response [200]>
>>> r2.history
[<Response [301]>, <Response [302]>]
>>> r1.history
[]
>>> type(r1.history)
<class 'list'>
>>> len(r1.history)
0
>>> if len(r1.history) == 0:
...     print('link in tact')
...
link in tact
>>> r2
<Response [200]>
>>> r2.history
[<Response [301]>, <Response [302]>]
>>> type(r2.history)
<class 'list'>
>>> len(r2.history)
2
>>> r3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'r3' is not defined
>>>
