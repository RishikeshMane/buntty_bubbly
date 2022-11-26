import csv

with open("./winequality-red.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)