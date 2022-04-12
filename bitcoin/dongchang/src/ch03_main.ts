import { FieldElement } from './field';
import { Point } from './point';

export function ch03_01() {
  const prime = 223;

  const a = 192;
  const b = 105;
  // const a = 17;
  // const b = 56;
  // const a = 200;
  // const b = 119;
  // const a = 1;
  // const b = 193;
  // const a = 42;
  // const b = 99;

  const x1 = new FieldElement(a, prime);
  const y1 = new FieldElement(b, prime);

  const p1 = new Point(x1, y1, 0, 7);
}

export function ch03_02() {
  const prime = 223;

  const a = 170;
  const b = 142;
  const c = 60;
  const d = 139;

  const x1 = new FieldElement(a, prime);
  const y1 = new FieldElement(b, prime);

  const x2 = new FieldElement(c, prime);
  const y2 = new FieldElement(d, prime);

  const p1 = new Point(x1, y1, 0, 7);
  const p2 = new Point(x2, y2, 0, 7);

  console.log(p1.add(p2)); // (220,181)
}

export function ch03_03() {
  const prime = 223;

  const a = 192;
  const b = 105;

  const x1 = new FieldElement(a, prime);
  const y1 = new FieldElement(b, prime);

  const p1 = new Point(x1, y1, 0, 7);

  console.log(p1);
}

export function ch03_05() {
  const prime = 223;

  const a = 15;
  const b = 86;

  const x1 = new FieldElement(a, prime);
  const y1 = new FieldElement(b, prime);
  const inf = new FieldElement(Infinity, prime);

  const p1 = new Point(x1, y1, 0, 7);
  const infP = new Point(inf, inf, 0, 7);

  let product = p1;
  let count = 1;

  while (product.isNotEqual(infP)) {
    product = product.add(p1);
    count++;
  }

  console.log(count);
}
