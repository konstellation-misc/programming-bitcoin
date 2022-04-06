# Excercise 1
from ecc import PrivateKey

def get_uncompressed_sec_from_priv_secret(secret, compressed):
    priv = PrivateKey(secret)
    point = priv.point
    sec = point.sec(compressed=compressed)
    return sec.hex()

num = 5000
sec = get_uncompressed_sec_from_priv_secret(num, False)
print("1.1", num, sec)

num = 2018**5
sec = get_uncompressed_sec_from_priv_secret(num, False)
print("1.2", num, sec)

num = 0xdeadbeef12345
sec = get_uncompressed_sec_from_priv_secret(num, False)
print("1.3", num, sec)

print()

# Exercise 2
from ecc import PrivateKey

def get_uncompressed_sec_from_priv_secret(secret, compressed):
    priv = PrivateKey(secret)
    point = priv.point
    sec = point.sec(compressed=compressed)
    return sec.hex()

num = 5001
sec = get_uncompressed_sec_from_priv_secret(num, True)
print("2.1", num, sec)

num = 2019**5
sec = get_uncompressed_sec_from_priv_secret(num, True)
print("2.2", num, sec)

num = 0xdeadbeef54321
sec = get_uncompressed_sec_from_priv_secret(num, True)
print("2.3", num, sec)
