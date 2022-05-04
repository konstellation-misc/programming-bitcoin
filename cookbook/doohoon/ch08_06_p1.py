class managed_attr:
    def __init__(self):
        self.__example = "what"

    @property
    def example(self):
        return self.__example

    @example.setter
    def example(self, str):
        self.__example = str

a = managed_attr()
print(a.example)
a.example = "what is that?"
print(a.example)