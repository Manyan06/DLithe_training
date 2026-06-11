#RUN csv_fileCreation 1st

import csv
file=open("students.csv", "r")
reader = csv.reader(file)
for row in reader:
  print(row)
file.close()