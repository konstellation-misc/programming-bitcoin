import { FieldElement } from "./field"

function ex01() {
  const a = new FieldElement(7, 13)
  const b = new FieldElement(6, 13)

  console.log(a.isEqual(b)) // false
  console.log(a.isNotEqual(b)) // true
  console.log(a.isEqual(a)) // true
  console.log(a.isNotEqual(a)) // false
}

function ex02(){
  const a = new FieldElement(44, 57)
  const b = new FieldElement(33, 57)

  console.log(a.add(b))
}

function ex03(){
  const a = new FieldElement(9, 57)
  const b = new FieldElement(86, 57)

  console.log(a.sub(b))
}

function ex04() {
  const a = new FieldElement(95, 97)
  // const b = new FieldElement(8, 19)
  const c = new FieldElement(12, 97)
  const d = new FieldElement(77, 97)

  console.log(a.mul(new FieldElement(45,97)).mul(new FieldElement(31, 97)))
  console.log(c.exp(7).mul(d.exp(49)))
}

function main() {
  // ex01()
  // ex02()
  // ex03()
  ex04()
}

main()