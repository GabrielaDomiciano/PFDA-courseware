# Simple program to read a csv file as a dictionary
# Author Andrew Beatty

import csv

FILENAME= "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        print (line)
        count +=1
    print (f"average is {total/(count)}") # why is there no -1 this time?