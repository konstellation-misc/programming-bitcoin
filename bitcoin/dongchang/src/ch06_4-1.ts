const hash160 = (element) => {
  return element
}

// any
const op_hash160 = (stack: Array<any>) => {
  if(stack.length < 1){
    return false
  } else {
    const element = stack[stack.length - 1]
    stack.pop()
    stack.push(element(element))
    return true
  }
}

const OP_CODE_FUNCTIONS = {
  170: op_hash160,
}