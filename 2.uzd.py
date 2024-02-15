import csv
with open('2. kollonas teksta saturs.csv') as file:
 lasit = csv.reader(file)
for row in lasit:
 print(row[2])