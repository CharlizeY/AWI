import csv
import sys
import requests

x = 1
failures = 0
URLs = []

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count = line_count + 1
        ArtURL = str(row[9])
        URL = row[9]
        URLs.append(URL)
print(line_count)

for i in range(1,line_count):
    print(x)
    x = x + 1
    Req = requests.get(URLs[i])
    History = Req.history
    for history in History:
        ResponseArray = []
        for character in str(history):
            try:
                ResponseArray.append(int(character))
            except:
                continue
        Response = ''
        for integer in ResponseArray:
            Response = Response + str(integer)
        if(Response == '302'):
            print('Art listing removed for line: ', x, '\n')
            failures = failures + 1
print('Number of failures :', failures)
