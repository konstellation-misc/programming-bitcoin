formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date: 
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == "":
            code = "ymd"
        formated_date = formats[code]
        return formated_date.format(d=self)

if __name__ == "__main__":
    d = Date(2022, 3, 16)
    res = format(d, "dmy")
    print(res)