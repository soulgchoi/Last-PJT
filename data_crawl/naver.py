import requests
import csv
from decouple import config

def send_naver_movie(movie_name):
    BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
    URL = BASE_URL + '?query=' + movie_name

    headers = {
        'X-Naver-Client-Id': 'eA8YKSyNRxTyuApSMeni',
        'X-Naver-Client-Secret': 'ZQ86ZIboif',
    }

    return requests.get(URL, headers=headers).json()

# print(send_naver_movie('완벽한 타인'))

# names = open('test3.csv', 'r', encoding='utf-8')
# names_reader = csv.DictReader(names)

# img = open('test5.csv', 'w', encoding='utf-8', newline='')
# fieldname = ['poster_url']
# cw_img = csv.DictWriter(img, fieldnames=fieldname)
# cw_img.writeheader()

names = open('movienames3.csv', 'r', encoding='utf-8')
names_reader = csv.DictReader(names)

img = open('movieimages5.csv', 'w', encoding='utf-8', newline='')
fieldname = ['poster_url']
cw_img = csv.DictWriter(img, fieldnames=fieldname)
cw_img.writeheader()

i = 3394
for name in names_reader:
    movieNm, year = name['movieNm'], name['years']

    data = send_naver_movie(movieNm).get('items')

    res = {}

    for d in data:
        # print(d['title'])
        if f'<b>{movieNm}</b>' == d['title'] and d['pubDate'] == year:
            res['poster_url'] = d['image']
            break
    cw_img.writerow(res)
    i += 1
    print(i)


# send data 받아서, 개봉년도가 같을 때 맞는 데이터 > 