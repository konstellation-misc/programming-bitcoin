import hashlib

from unittest import TestCase

from ecc import (
    S256Point,
    Signature,
)

from helper import (
    hash160,
    hash256,
)


def encode_num(num):
    if num == 0:
        return b''
    abs_num = abs(num)
    negative = num < 0
    result = bytearray()
    while abs_num:
        result.append(abs_num & 0xff)
        abs_num >>= 8
    if result[-1] & 0x80:
        if negative:
            result.append(0x80)
        else:
            result.append(0)
    elif negative:
        result[-1] |= 0x80
    return bytes(result)


# tag::source1[]
def op_dup(stack):
    if len(stack) < 1:  # <1>
        return False
    stack.append(stack[-1])  # <2>
    return True
# end::source1[]


# tag::answer1[]
def op_hash160(stack):
    if len(stack) < 1:
        return False
    element = stack.pop()
    h160 = hash160(element)
    stack.append(h160)
    return True
# end::answer1[]


# tag::source2[]
def op_hash256(stack):
    if len(stack) < 1:
        return False
    element = stack.pop()
    stack.append(hash256(element))
    return True
# end::source2[]