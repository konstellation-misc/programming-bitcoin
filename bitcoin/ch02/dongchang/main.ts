import { FieldElement } from "../../ch01/dongchang/field";
import { Point } from "./point";

export function ch02_01(){
  const a = 5
  const b = 7

  // const point1 = new Point(2, 4, a, b)
  // console.log(point1) // Error
  // const point2 = new Point(-1, -1, a, b)
  // console.log(point2)
  // const point3 = new Point(18, 77, a, b)
  // console.log(point3)
  // const point4 = new Point(5 , 7, a, b)
  // console.log(point4) // Error
  
}

export function ch02_04(){
  const a = 5
  const b = 7
  // const p1 = new Point(2,5, a, b)
  // const p2 = new Point(-1,-1, a, b)

  // console.log(p1.add(p2))
}

export function ch02_06(){
  const a = 5
  const b = 7
  const prime = 18
  const p1 = new Point(new FieldElement(2,prime), new FieldElement(2,prime), a, b)
  // const p1 = new Point(-1,-1, a, b)

  console.log(p1.add(p1))
}