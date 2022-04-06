# Excercise 1
from ecc import PrivateKey

def get_uncompressed_sec_from_priv_secret(secret):
    priv = PrivateKey(secret)
    point = priv.point
    sec = point.sec(compressed=False)
    return sec.hex()

# 1.1
num = 5000
sec = get_uncompressed_sec_from_priv_secret(num)
print(num, sec)

# 1.2
num = 2018**5
sec = get_uncompressed_sec_from_priv_secret(num)
print(num, sec)

# 1.3
num = 0xdeadbeef12345
sec = get_uncompressed_sec_from_priv_secret(num)
print(num, sec)
