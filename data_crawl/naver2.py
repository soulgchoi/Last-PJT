from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import time

data = open('movieimages_.csv', 'r', encoding='utf-8')
reader = csv.DictReader(data)


result = open('moviedescription.csv', 'w', encoding='utf-8', newline='')
fieldnames = ['head', 'description']
writer = csv.DictWriter(result, fieldnames=fieldnames)
writer.writeheader()

i = 0

for row in reader:
    time.sleep(0.5)
    link = row['link']

    res = {}

    if link == '':
        res['head'] = ''
        res['description'] = ''
    else:
        html = urlopen(link)

        bsObject = BeautifulSoup(html, "html.parser")
        description1 = bsObject.body.find('h5', 'h_tx_story')
        description2 = bsObject.body.find('p', 'con_tx')
        
        try: 
            res['head'] = description1.get_text()
        except AttributeError:
            res['head'] = ''
        try:
            res['description'] = description2.get_text()
        except AttributeError:
            res['description'] = ''

    i += 1
    print(i)
    writer.writerow(res)

data.close()
reder.close()