import { FieldElement } from './field';
import { Point } from './point';

export function ch02_01() {
  const a = 5;
  const b = 7;

  // const point1 = new Point(2, 4, a, b)
  // console.log(point1) // Error
  // const point2 = new Point(-1, -1, a, b)
  // console.log(point2)
  // const point3 = new Point(18, 77, a, b)
  // console.log(point3)
  // const point4 = new Point(5 , 7, a, b)
  // console.log(point4) // Error
}

export function ch02_04() {
  const a = 5;
  const b = 7;
  // const p1 = new Point(2,5, a, b)
  // const p2 = new Point(-1,-1, a, b)

  // console.log(p1.add(p2))
}

export function ch02_06() {
  const a = 0;
  const b = 7;
  const prime = 223;
  const p1 = new Point(new FieldElement(47, prime), new FieldElement(71, prime), a, b);
  // const p1 = new Point(-1,-1, a, b)

  const product = p1
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1)
    .add(p1);
  console.log(product.x.num, product.y.num, p1.x.num, p1.y.num);
}
