import { Point } from "./point";

function ex01(){
  const a = 5
  const b = 7

  // const point1 = new Point(2, 4, a, b)
  // console.log(point1) // Error
  const point2 = new Point(-1, -1, a, b)
  console.log(point2)
  const point3 = new Point(18, 77, a, b)
  console.log(point3)
  // const point4 = new Point(5 , 7, a, b)
  // console.log(point4) // Error
  
}

function ex04(){
  const a = 5
  const b = 7
  const p1 = new Point(2,5, a, b)
  const p2 = new Point(-1,-1, a, b)

  console.log(p1.add(p2))
}

function ex06(){
  const a = 5
  const b = 7
  const p1 = new Point(-1,-1, a, b)

  console.log(p1.add(p1))
}

function main() {
  try{
    // ex01()
    // ex04()
    ex06()
  }catch(e){
    console.log(e.message)
  }
}

main()