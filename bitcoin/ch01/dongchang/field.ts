function addMod(x: number, y: number, n: number)
{
    // Precondition: x<n, y<n
    // If it will overflow, use alternative calculation
    if (x + y <= x) x = x - (n - y) % n;
    else x = (x + y) % n;
    return x;
}

function sqrMod(a: number, n: number)
{
    var b: number;
    var sum = 0;

    // Make sure original number is less than n
    a = a % n;

    // Use double and add algorithm to calculate a*a mod n
    for (b = a; b != 0; b >>= 1) {
        if (b & 1) {
            sum = addMod(sum, a, n);
        }
        a = addMod(a, a, n);
    }
    return sum;
}

function powExp(base: number, ex: number, mo: number) {
  var r: number;
  if(ex === 0) 
      return 1;
  else if(ex % 2 === 0) {
      r = powExp(base, ex/2, mo) % mo ;
      // return (r * r) % mo;
      return sqrMod(r, mo);
  }else 
      return (base * powExp(base, ex - 1, mo)) % mo;
}

export class FieldElement {
  num: number
  prime: number

  constructor(num: number, prime: number){
    this.num = num
    this.prime = prime
  }

  isEqual = (other: FieldElement): boolean => {
    return this.num === other.num && this.prime === other.prime
  }

  isNotEqual = (other: FieldElement): boolean => {
    return this.num !== other.num || this.prime !== other.prime
  }

  add = (other: FieldElement): FieldElement => {
    if(this.prime != other.prime){
      throw Error('Cannot add two number in different Fields')
    }

    const number = (this.num + other.num) % this.prime
    
    return new FieldElement(number, this.prime)
  }

  sub = (other: FieldElement): FieldElement => {
    if(this.prime != other.prime){
      throw Error('Cannot add two number in different Fields')
    }

    const beforeNegation = (this.num - other.num) % this.prime
    const afterNegation = beforeNegation > 0 ? beforeNegation : beforeNegation + this.prime

    return new FieldElement(afterNegation, this.prime)
  }

  mul = (multiplier: FieldElement): FieldElement => {
    if(this.prime != multiplier.prime) {
      throw Error('Cannot add two number in different Fields')
    }

    const number = this.num * multiplier.num % this.prime

    return new FieldElement(number, this.prime)
  }

  exp = (exponent: number): FieldElement => {
    const n = exponent % (this.prime - 1)
    const number = powExp(this.num, n, this.prime)

    return new FieldElement(number, this.prime)
  }
}