
import __future__ import print_function

__description__  = 'Read big file using class + slots + cache '

class Row(object):
    __slots__ = ('route', 'date', 'daytype', 'rides')
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_instances(filename):
    records = []
    cache = { }    # String-cache (interning)
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip (not data)
        for row in rows:
            route = cache.setdefault(row[0], row[0])
            date = cache.setdefault(row[1], row[1])
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)  #instance
            records.append(record)
    return records


def main():
	rows = read_rides_as_instances('ctabus.csv')



if __name__ == '__main__':
	main()
	
