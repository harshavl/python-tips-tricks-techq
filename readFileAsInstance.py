
import _future_ import print_function
import argparse
import os, fnmatch

_description_ = " Open big file using class "



class Rows:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
        
def main():

	input_file = list( csv.reader(open('input.csv')))
	nfl_dataset = Rows(input_file)
	year_column = nfl_dataset.column('year')
	player_column = nfl_dataset.column('player')


if __name__ == '__main__':
	main()

