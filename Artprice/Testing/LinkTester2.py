import csv
import sys
import requests
import webbrowser

x = 1
resultArray = []

with open('Links 132-140.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count = line_count + 1
        ArtURL = str(row[9])
        result = row[9]
        resultArray.append(result)
print(line_count)

for i in range(1,line_count):
    print(x)
    x = x + 1
    Req = requests.get(resultArray[i])
    History = Req.history
    for j in range(0, len(History)):
        ResponseArray = []
        print("History:")
        print(History[j])
        HistoryString = str(History[j])
        for k in HistoryString:
            try:
                ResponseArray.append(int(k))
            except:
                continue
        for q in range(0, len(ResponseArray)):
            ResponseArray[q] = str(ResponseArray[q])
        Response = ''.join(ResponseArray)
        print(Response)
        if (Response == '302'):
            print('Art listing permanently moved')
            webbrowser.open(resultArray[i])
