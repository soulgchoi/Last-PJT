import requests
import csv

# key = 'fb87484ce21fa7529722b4d19c29bfb7'
key = '5bde81c4c7e47415a501a03c55d15832'  # 오빠꺼
req_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd='


# test4 = open('test4.csv', 'w', encoding='utf-8', newline='')
# fieldnames = ['genres']
# cw_test4 = csv.DictWriter(test4, fieldnames=fieldnames)
# cw_test4.writeheader()
genres = open('genres3.csv', 'w', encoding='utf-8', newline='')
fieldnames = ['genres']
cw_genres = csv.DictWriter(genres, fieldnames=fieldnames)
cw_genres.writeheader()

i = 4759
movieCd = open('moviecodes2.csv', 'r', encoding='utf-8')
Cdreader = csv.DictReader(movieCd)
for row in Cdreader:
    code = row['movieCd']
    URL = req_URL + code
    genre = {'genres': []}
    data = requests.get(URL).json().get('movieInfoResult').get('movieInfo').get('genres')
    for d in data:
        genre['genres'] += [d['genreNm']]
    i += 1
    print(i)
    genre['genres'] = ','.join(genre['genres'])
    cw_genres.writerow(genre)

genres.close()
movieCd.close()
