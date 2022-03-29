"""
When you define __slots__, Python use more compact internal representation
for instances. Instead of each instance consisting of a dictionary, instances are build around
a small fixed-sized array, much like tuple or list.

A side effect is that you can no longer add new attributes
"""

class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

