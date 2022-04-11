import { FieldElement } from './field';
export class Point {
  x: FieldElement;
  y: FieldElement;
  a: number;
  b: number;
  inf: FieldElement;

  constructor(x: FieldElement, y: FieldElement, a: number, b: number) {
    this.x = x;
    this.y = y;
    this.a = a;
    this.b = b;
    this.inf = new FieldElement(Infinity, x.prime);

    if (this.x.num === Infinity && this.y.num === Infinity) {
      return;
    } else {
      if (y.exp(2).isNotEqual(x.exp(3).add(x.mul(a)).add(b))) {
        throw new Error(`(${x}, ${y}) is not on the curve`);
      }
    }
  }

  isEqual = (other: Point) => {
    return this.x.isEqual(other.x) && this.y.isEqual(other.y) && this.a === other.a && this.b === other.b;
  };

  isNotEqual = (other: Point) => {
    return this.x.isNotEqual(other.x) || this.y.isNotEqual(other.y) || this.a !== other.a || this.b !== other.b;
  };

  add = (other: Point) => {
    if (this.a !== other.a || this.b !== other.b) {
      throw new Error(`${this}, ${other} are not on the same curve`);
    }

    if (this.x.num === Infinity) {
      return other;
    }

    if (other.x.num === Infinity) {
      return this;
    }

    if (this.x.isEqual(other.x)) {
      if (this.y.isEqual(other.y)) {
        if (this.y.num === 0) {
          return new Point(this.inf, this.inf, this.a, this.b);
        } else {
          const s = this.x.exp(2).mul(3).add(this.a).div(this.y.mul(2));
          const newX = s.exp(2).sub(this.x.mul(2));
          const newY = s.mul(this.x.sub(newX)).sub(this.y);

          return new Point(newX, newY, this.a, this.b);
        }
      } else {
        return new Point(this.inf, this.inf, this.a, this.b);
      }
    } else {
      const s = other.y.sub(this.y).div(other.x.sub(this.x));
      const newX = s.exp(2).sub(this.x).sub(other.x);
      const newY = s.mul(this.x.sub(newX)).sub(this.y);

      return new Point(newX, newY, this.a, this.b);
    }
  };
}
