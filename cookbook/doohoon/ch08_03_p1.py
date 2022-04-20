import requests

class WhatIsWithStatement:
    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.request_get = requests.get(self.target)
        return self.request_get

    def __exit__(self, type, value, trace):
        self.request_get.connection.close() # Is it really needed?, I'm not sure.

w = WhatIsWithStatement('https://www.google.com')
s = ""

with w:
    s = w.request_get.json()

print(s)