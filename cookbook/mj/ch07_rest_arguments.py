
"""Accepting any number of positional arguments"""
# NOTE: *argument can only appear as teh last positional argument

def average(first, *rest):
    item_count = 1 + len(first)
    total = first + sum(rest)

    return total  / item_count

# OR

def average(*numbers):
    return sum(numbers) / len(numbers)

def tes(a, *args, y):
    pass

def b(x, *args, **kwargs):
    pass

"""Accepting any number of keyword arguments"""
# Use an arguments that starts with **

import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()] 
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                      name=name,
                      attrs=attr_str,
                      value=html.escape(value))
    return element


# NOTE: Positional arguments cannot appear before keyword-arguments
def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


