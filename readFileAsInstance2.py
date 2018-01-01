


import __future__ import print_function
import csv

__description__ = 'Read file as an instance'

class Row(object):
    __slots__ = ('col1', 'col2', 'col3', 'col4')
    def __init__(self, col1, col2, col3, col4):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.col4 = col4


def read_as_instances(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   
        for row in rows:
            col1 = row[0]
            col2 = row[1]
            col3 = row[2]
            col4 = int(row[3])
            record = Row(col1, col2, col3, col4)  #instance
            yield record

rows = read_col4_as_instances('ctabus.csv')

def find_col1(rows, col1):
    for row in rows:
        if row.col1 == col1:
            yield row

def col2_col4(rows):
    for row in rows:
        yield (row.col4, row.col2)

def main():
	rows = read_col4_as_instances('ctabus.csv')

	rt22 = find_col1(rows, '22')
	data = col2_col4(rt22)
	print(max(data))



if __name__ == '__main__':
	main()

