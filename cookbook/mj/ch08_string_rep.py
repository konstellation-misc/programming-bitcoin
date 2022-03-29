
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        """
        returns the code representation of an instance and it is usually a text 
        you would type to re-create the instance
        """
        return f"pair({self.x}, {self.y})"
    def __str__(self):
        """
        converts the instance to a string, and it is output producted by the str() and print
        """
        return f"({self.x}, {self.y})"


pair = Pair(10, 20)

if __name__ == "__main__":
    pass