import csv

f1 = open("data//yosar_located.csv")
f2 = open("data//raw//yosar_missing_inspection.csv")

reader1 = csv.reader(f1)
reader2 = csv.reader(f2)

for rows in reader1:
    print(rows) 