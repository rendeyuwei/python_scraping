import csv

output_list = ['1', '2', '3', '4']
with open('test2.csv', 'a+', newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(output_list)
