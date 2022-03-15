def op_checksig(stack, z):
    if len(stack) < 2:
        return False
    sec = stack.pop()
    der = stack.pop()
    der = der[:-1]
    try:
        point = S256Point.parse(sec)
        sig = Signature.parse(der)
    except (ValueError, SyntaxError) as e:
        return False
    if point.verify(z, sig):
        stack.append(encode_num(1))
    else:
        stack.append(encode_num(0))
    return True