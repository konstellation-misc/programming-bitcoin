from inspect import Signature, Parameter

params = [
    Parameter("x", Parameter.POSITIONAL_OR_KEYWORD),
    Parameter("y", Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter("z", Parameter.KEYWORD_ONLY, default=None),
]
sig = Signature(params)
print(sig)


def f():
    pass

"""
# Question 1 What will happen?

help(f)

f.__signature__ = sig
help(f)

f(x=1, y=2, z=3)
"""


def make_sig(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(params)


class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        # TODO
        pass


class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
        _fields = ['x', 'y']
