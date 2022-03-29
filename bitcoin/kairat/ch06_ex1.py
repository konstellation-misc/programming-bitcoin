def op_hash160(stack):
    if len(stack) < 1:
        return False
    element = stack.pop()
    stack.append(hash160(element))
    return True
