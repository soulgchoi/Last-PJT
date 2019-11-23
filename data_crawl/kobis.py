import requests
import csv
from datetime import datetime, timedelta

key = 'fb87484ce21fa7529722b4d19c29bfb7'
req_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}'

date = []
for i in range(520):
    d = datetime(2019, 11, 17) - timedelta(weeks=i)
    date.append(d.strftime('%Y%m%d'))

# URL = req_URL + key + '&targetDt=' + date + '&weekGb=0'

# test1 = open('test.csv', 'w', encoding='utf-8', newline='')
# fieldnames1 = ['showRange', 'movieNm', 'rank', 'movieCd', 'openDt', 'audiAcc']
# cw_test1 = csv.DictWriter(test1, fieldnames=fieldnames1)
# cw_test1.writeheader()

# test2 = open('test2.csv', 'w', encoding='utf-8', newline='')
# fieldnames2 = ['movieCd']
# cw_test2 = csv.DictWriter(test2, fieldnames=fieldnames2)
# cw_test2.writeheader()

# test3 = open('test3.csv', 'w', encoding='utf-8', newline='')
# fieldnames3 = ['movieNm', 'years']
# cw_test3 = csv.DictWriter(test3, fieldnames=fieldnames3)
# cw_test3.writeheader()


movies = open('movies.csv', 'w', encoding='utf-8', newline='')
fieldnames1 = ['showRange', 'movieNm', 'rank', 'movieCd', 'openDt', 'audiAcc']
cw_movies = csv.DictWriter(movies, fieldnames=fieldnames1)
cw_movies.writeheader()

moviecodes = open('moviecodes.csv', 'w', encoding='utf-8', newline='')
fieldnames2 = ['movieCd']
cw_moviecodes = csv.DictWriter(moviecodes, fieldnames=fieldnames2)
cw_moviecodes.writeheader()

movienames = open('movienames.csv', 'w', encoding='utf-8', newline='')
fieldnames3 = ['movieNm', 'years']
cw_movienames = csv.DictWriter(movienames, fieldnames=fieldnames3)
cw_movienames.writeheader()

res1 = {}
movie_codes = {}
movie_name = {}
for day in date:
    URL = req_URL + '&targetDt=' + day + '&weekGb=0'
    # print(URL)
    data = requests.get(URL).json()
    data1 = data.get('boxOfficeResult')
    for movie in data1.get('weeklyBoxOfficeList'):
        res1['showRange'] = data1.get('showRange')
        res1['movieNm'] = movie.get('movieNm')
        res1['rank'] = movie.get('rank')
        res1['movieCd'] = movie.get('movieCd')
        res1['openDt'] = movie.get('openDt')
        res1['audiAcc'] = movie.get('audiAcc')
        movie_codes['movieCd'] = movie.get('movieCd')
        movie_name['movieNm'] = movie.get('movieNm')
        movie_name['years'] = movie.get('openDt')[:4]
        # print(res1)
        cw_movies.writerow(res1)
        cw_moviecodes.writerow(movie_codes)
        cw_movienames.writerow(movie_name)

movies.close()
moviecodes.close()
movienames.close()
