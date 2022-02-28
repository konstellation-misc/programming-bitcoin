import csv 
from pprint import pprint

def read_csv(file_path):
    with open(file_path, "r") as file:
        csv_content = csv.reader(file)
        return [row for row in csv_content]

def csv_to_dict(file_path):
    with open(file_path, "r") as file:
        res = csv.DictReader(file)
        return [row for row in res]

def data_to_csv(file_path):
    headers = ["Symbol", "Price", "Date", "Time", "Change", "Volume"]
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
           ]
    with open(file_path, "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)
        csv_writer.writerows(rows)

    return True


def dict_csv(file_path):
    headers = ["Symbol", "Price", "Date", "Time", "Change", "Volume"]
    rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
              'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
            {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
              'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
            {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
              'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
            ]

    with open(file_path, "w") as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    file_path = "stocks.csv"
    content = csv_to_dict(file_path)
    pprint(content)

__all__ = ['read_csv']