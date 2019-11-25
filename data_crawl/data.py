import csv

data = open('sample1.csv', 'r', encoding='utf-8')
reader = csv.DictReader(data)

sample2 = open('sample2.csv', 'w', encoding='utf-8', newline='')
writer = csv.DictWriter(sample2)


movies = ['start']

for row in reader:
    print(row)