"""
Question 1


See this
```
class Person:
    pass
person1 = Person()

print(type(1))
print(type(person1))

print(type(type(1)))     # or print(type(int))
print(type(type(person)  # or print(type(Person))
```

What is `type()` ?
* Is it a function?
* Is it a class?


Question 2
What is weakref?
"""

import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name
