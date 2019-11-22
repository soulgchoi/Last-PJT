import requests
import csv
from datetime import datetime, timedelta

key = 'fb87484ce21fa7529722b4d19c29bfb7'
req_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}'

date = []
for i in range(20):
    d = datetime(2019, 11, 17) - timedelta(weeks=i)
    date.append(d.strftime('%Y%m%d'))

# URL = req_URL + key + '&targetDt=' + date + '&weekGb=0'

with open('test.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['showRange', 'movieNm', 'rank', 'movieCd', 'openDt', 'audiAcc']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    result = {}
    # movie_codes = []
    for day in date:
        URL = req_URL + '&targetDt=' + day + '&weekGb=0'
        # print(URL)
        data = requests.get(URL).json()
        data1 = data.get('boxOfficeResult')
        for movie in data1.get('weeklyBoxOfficeList'):
            result['showRange'] = data1.get('showRange')
            result['movieNm'] = movie.get('movieNm')
            result['rank'] = movie.get('rank')
            result['movieCd'] = movie.get('movieCd')
            result['openDt'] = movie.get('openDt')
            result['audiAcc'] = movie.get('audiAcc')
            # print(result)
            writer.writerow(result)


