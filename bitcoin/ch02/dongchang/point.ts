export class Point {
  x: number
  y: number
  a: number
  b: number

  constructor(x: number, y: number, a: number, b: number){
    this.x = x
    this.y = y
    this.a = a
    this.b = b
    if(this.x === Infinity && this.y === Infinity){
      return
    }

    if (this.y**2 !== this.x**3 + a*x + b){
      throw new Error(`(${x}, ${y}) is not on the curve`)
    }
  }

  isEqual = (other: Point) => {
    return this.x === other.x && this.y === other.y && this.a === other.a && this.b === other.b
  }

  isNotEqual = (other: Point) => {
    return this.x !== other.x || this.y !== other.y || this.a !== other.a || this.b !== other.b
  }

  add = (other: Point) => {
    if (this.a !== other.a || this.b !== other.b) {
      throw new Error(`${this}, ${other} are not on the same curve`)
    }

    if(this.x === Infinity){
      return other
    }

    if(other.x === Infinity){
      return this
    }

    if(this.x === other.x){
      if(this.y === other.y){
        if(this.y === 0){
          return new Point(Infinity, Infinity, this.a, this.b)
        } else {
          const s = (3 * (this.x**2) + this.a) / (2 * this.y)
          const newX = s**2 - (2 * this.x)
          const newY = s*(this.x - newX) - this.y

          return new Point(newX, newY, this.a, this.b)
        }
      } else {
        return new Point(Infinity, Infinity, this.a, this.b)
      }
    } else {
      const s = (other.y - this.y) / (other.x - this.x)
      const newX = s**2 - this.x - other.x
      const newY = s * (this.x - newX) - this.y

      return new Point(newX, newY, this.a, this.b)
    }
  }
}