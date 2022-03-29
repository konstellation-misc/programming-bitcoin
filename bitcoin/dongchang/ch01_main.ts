import { FieldElement } from "./field"

export function ch01_01() {
  const a = new FieldElement(7, 13)
  const b = new FieldElement(6, 13)

  console.log(a.isEqual(b)) // false
  console.log(a.isNotEqual(b)) // true
  console.log(a.isEqual(a)) // true
  console.log(a.isNotEqual(a)) // false
}

export function ch01_02(){
  const a = new FieldElement(44, 57)
  const b = new FieldElement(33, 57)

  console.log(a.add(b))
}

export function ch01_03(){
  const a = new FieldElement(9, 57)
  const b = new FieldElement(86, 57)

  console.log(a.sub(b))
}

export function ch01_04() {
  const a = new FieldElement(95, 97)
  // const b = new FieldElement(8, 19)
  const c = new FieldElement(12, 97)
  const d = new FieldElement(77, 97)

  console.log(a.mul(45).mul(31))
  console.log(c.exp(7).mul(d.exp(49)))
}

export function ch01_08(){
  const prime = 31
  const a = new FieldElement(3, prime)
  const b = new FieldElement(24, prime)

  const c = new FieldElement(17, prime)
  const d = new FieldElement(4, prime)

  console.log(a.div(b), a.div(24))
  console.log(c.exp(-3))
  console.log(d.exp(-4).mul(11))
}