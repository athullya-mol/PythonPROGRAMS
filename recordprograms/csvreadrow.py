import csv
with open ('dept.csv',newline='')as csvfile:
    data=csv.reader(csvfile,delimiter=' ',quotechar='|')
    for row in data:
        print(','.join(row))
