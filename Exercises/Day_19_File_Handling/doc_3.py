import csv

list_test = ['1', '2', '3', '4']
with open('./files/test_csv.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Test', row)
            print(f'Columns name are: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}')
        line_count += 1