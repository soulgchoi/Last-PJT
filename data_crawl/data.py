import csv

# data = open('sample1.csv', 'r', encoding='utf-8')
# reader = csv.DictReader(data)

# sample2 = open('sample2.csv', 'w', encoding='utf-8', newline='')
# fieldnames = ['showRange', 'rank', 'movieNm']
# writer = csv.DictWriter(sample2, fieldnames=fieldnames)
# writer.writeheader()

# movies = ['start']

# for row in reader:
#     name1 = row['movieNm']

#     sample2_res = {}

#     if name1 not in movies:
#         movies += [name1]
    
#     sample2_res['showRange'] = row['showRange']
#     sample2_res['rank'] = row['rank']
#     sample2_res['movieNm'] = movies.index(row['movieNm'])

#     writer.writerow(sample2_res)


# data.close()
# sample2.close()

data = open('movies_fin_fin_fin.csv', 'r', encoding='utf-8')
reader = csv.DictReader(data)

movie_id = open('movie_id.csv', 'w', encoding='utf-8', newline='')
fieldnames = ['showRange', 'movieNm', 'movieCd', 'rank', 'movieId']
writer = csv.DictWriter(movie_id, fieldnames=fieldnames)
writer.writeheader()

# movies = ['start']
codes = ['0']
for row in reader:
    code = row['movieCd']

    id_res = {}

    if code not in codes:
        codes += [code]

    id_res['showRange'] = row['showRange']
    id_res['movieNm'] = row['movieNm']
    id_res['movieCd'] = code
    id_res['rank'] = row['rank']
    id_res['movieId'] = codes.index(row['movieCd'])

    writer.writerow(id_res)


data.close()
movie_id.close()