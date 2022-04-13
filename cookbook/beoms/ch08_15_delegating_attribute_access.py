# When you want to delegate method implementations to another code
# you may want to use a proxy pattern. This is similar to inheritance,
# but you may want to use it when you have more control. For example,
# you can get around the fall back mechanism (MRO) of inheritacne by using
# this pattern. Please refer to the discussion in the book.

class A:
    # Question: What is bound method?
    def spam(self, x):
        print("A spam", x)

    def foo(self):
        print("B foo")


# Implementing a proxy using `getattr`
class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        print("B")

    def __getattr__(self, name):
        ### IMPORTANT ###
        return getattr(self._a, name)

print("(1)")
b = B()
b.bar()
b.spam(42)
print()


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Question: Why do you think the author did this?
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)

# Question: how am i supposed to use Proxy?
