import csv

print('Reading as dicts with type conversion')
field_types = [ ('Symbol', str),
				('Price', float),
				('Date', str),
				('Time', str),
				('Change', float),
				('Volume', int) ]
with open('stocks.csv') as f:
	for row in csv.DictReader(f):
		row.update((key, conversion(row[key]))
			for key, conversion in field_types)
		print(row)