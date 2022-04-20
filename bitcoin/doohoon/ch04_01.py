from ecc import PrivateKey

private_key = PrivateKey(5000)

print(private_key.point.sec(compressed=False).hex())

private_key = PrivateKey(2018**5)

print(private_key.point.sec(compressed=False).hex())

private_key = PrivateKey(0xdeadbeef12345)

print(private_key.point.sec(compressed=False).hex())