import requests
import csv
from decouple import config

def send_naver_movie(movie_name):
    # naver_client_id = config('NAVER_CLIENT_ID')
    # naver_client_secret = config('NAVER_CLIENT_SECRET')
    BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
    URL = BASE_URL + '?query=' + movie_name

    headers = {
        'X-Naver-Client-Id': 'eA8YKSyNRxTyuApSMeni',
        'X-Naver-Client-Secret': 'ZQ86ZIboif',
    }

    return requests.get(URL, headers=headers).json()


with open('test.csv', 'r', encoding='utf-8') as f:
    with open('test2.csv', 'w', encoding='utf-')
    reader = csv.DictReader(f)
    for row in reader:




print(send_naver_movie('모아나').get('item'))

# send data 받아서, 개봉년도가 같을 때 맞는 데이터 > 