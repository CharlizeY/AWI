import csv
import requests
import webbrowser

x = 1
resultArray = []

with open('Links 141-642.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:

        ArtURL = str(row[9])
        result = row[9]
        resultArray.append(result)

for i in range(1,501):
    print(x)
    x = x + 1

    Req = requests.get(resultArray[i])
    History = Req.history
    if len(History) != 0:
        print('Webpage has been moved')
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
            if (Response == '301'):
                print('Webpage permanently moved')
                webbrowser.open(resultArray[i])
    else:
        print('Original webpage location in tact')
