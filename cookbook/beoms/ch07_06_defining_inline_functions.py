# One important use case for inline functions is sort

names = ['1_show', '5_me', '15_the', '20_money']
n = sorted(names, key=lambda x: x)
print(n)

# Question, we sort function receives key argument, not cmp?
