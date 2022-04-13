from ecc import PrivateKey

private_key = PrivateKey(5000)

print(private_key.point.sec(compressed=False).hex())