def str_sum(one, /, x) :
    try:
        assert type(one) == str
        assert type(x) == str
        return one + x
    except AssertionError:
        return ""

def str_sum2(one, *, x) :
    try:
        assert type(one) == str
        assert type(x) == str
        return one + x
    except AssertionError:
        return ""
    
print(str_sum("err", x="or"))
print(str_sum("err", "or"))

print(str_sum2("err", x="or"))
print(str_sum2("err", "or"))
