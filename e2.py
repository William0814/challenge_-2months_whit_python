import csv

with open('files/file.csv', 'r') as file:
    data = list(csv.reader(file))

print(data)