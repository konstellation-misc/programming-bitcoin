# Initial byte string
s = b'hello'
# Encode as hex
import binascii
h = binascii.b2a_hex(s)
print(h)

# Decode back to bytes
print(binascii.a2b_hex(h))


import base64
h = base64.b16encode(s)
print(h)

print(base64.b16decode(h))


import base64

a = base64.b64encode(s)
print(a)
print(base64.b64decode(a))