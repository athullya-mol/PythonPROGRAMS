import csv
with open('abcd.txt', mode='w') as outf:
    fieldnames = ['RollNo','Name', 'Department']
    content = csv.DictWriter(outf, fieldnames=fieldnames)
    content.writeheader()
    content.writerow({'RollNo':'18','Name': 'John', 'Department': 'MCA'})
    content.writerow({'RollNo':'1','Name': 'Amy', 'Department': 'IT'})
