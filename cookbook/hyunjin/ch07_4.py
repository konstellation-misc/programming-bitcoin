x = 42
def spam(a, b=x):
	print(a, b)
spam(1)

x = 30
spam(2)

x = [42]
def spam(a, b=x):
	print(a, b[0])
spam(1)

x[0] = 10
spam(2)