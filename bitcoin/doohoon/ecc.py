import hmac
from typing import Union, Optional

from random import randint
import hashlib


class FieldElement:
    def __init__(self, num: int, prime: int) -> None:
        # 입력값이 올바른지 검사
        if num >= prime or num < 0:
            error = f"Num {num} not in field range 0 to {prime - 1}"
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return f"FieldElement_{self.prime}({self.num})"

    def __eq__(self, other: Optional[any]) -> Optional[bool]:
        if other is None:
            return None
        # num, prime의 값이 서로 같은지 검사
        # a(FieldElement) == b(FieldElement)
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other: Optional[any]) -> Optional[bool]:
        if other is None:
            return None
        # num, prime의 값이 서로 다른지 검사
        # a(FieldElement) != b(FieldElement)
        return self.num != other.num and self.prime != other.prime

    def _arith_op(self, op:str, other: Optional[any]) -> int:
        if self.prime != other.prime:
            raise TypeError(f"Cannot {op} two numbers in different Fields")

        if op == "add":
            return self.num + other.num
        elif op == "sub":
            return self.num - other.num
        elif op == "mul":
            return self.num * other.num
        elif op == "div":
            return self.num / other.num
        elif op == "fdiv":
            return self.num // other.num

    def __add__(self, other: Optional[any]) -> Optional[any]:
        # 연산자, 피연산자의 위수가 다른지 검사(유한체에 포함 되어 있는지 아닌지 검사)
        # ((a) +_f(b)) % p
        num = self._arith_op("add", other) % self.prime
        # 그리고, 자신의 Class instance에 반환
        return self.__class__(num, self.prime)

    def __sub__(self, other: Optional[any]) -> Optional[any]:
        # 연산자, 피연산자의 위수가 다른지 검사(유한체에 포함 되어 있는지 아닌지 검사)
        # ((a) -_f(b)) % p
        num = self._arith_op("sub", other) % self.prime
        # 그리고, 자신의 Class instance에 반환
        return self.__class__(num, self.prime)

    def __mul__(self, other: Optional[any]) -> Optional[any]:
        # 연산자, 피연산자의 위수가 다른지 검사(유한체에 포함 되어 있는지 아닌지 검사)
        # ((a) *_f(b)) % p
        num = self._arith_op("mul", other) % self.prime
        # 그리고, 자신의 Class instance에 반환
        return self.__class__(num, self.prime)

    def __truediv__(self, other: Optional[any]) -> Optional[any]:
        # 연산자, 피연산자의 위수가 다른지 검사(유한체에 포함 되어 있는지 아닌지 검사)
        # ((a) /_f(b)) % p
        num = self._arith_op("div", other) % self.prime
        # 그리고, 자신의 Class instance에 반환
        return self.__class__(num, self.prime)

    # 없는 것.
    def __floordiv__(self, other: Optional[any]) -> Optional[any]:
        # 연산자, 피연산자의 위수가 다른지 검사(유한체에 포함 되어 있는지 아닌지 검사)
        # ((a) //_f(b)) % p
        num = self._arith_op("fdiv", other) % self.prime
        # 그리고, 자신의 Class instance에 반환
        return self.__class__(num, self.prime)

    def __pow__(self, exponent: int) -> Optional[any]:
        # 거듭제곱 수의 위수가 다른지 검사함(거듭제곱 수도 유한체에 포함 되어 있는지 아닌지 검사, 지수는 유한체에 포함되어 있지 않아도 상관 없음)
        # ((a) ^_f(b)) % p
        # 페르마의 소정리에 해당 됨
        # num = (self.num ** exponent) % self.prime
        print(f"{self.prime} {type(self.prime)}")
        num = pow(self.num, exponent % (self.prime - 1), self.prime)
        return self.__class__(num, self.prime)

    def __rmul__(self, coefficient: int) -> Optional[any]:
        num = (self.num * coefficient) % self.prime
        return self.__class__(num, self.prime)



class Point:
    def __init__(self, x: int, y: int, a: int, b: int) -> None:
        self.x = x
        self.y = y
        self.a = a
        self.b = b

        if self.x is None and self.y is None:
            return

        # y^2 = x^3 + ax + b에 만족하지 않는다면?
        # 곧 타원함수의 좌표 안에 해당 좌표가 포함되어 있지 않으므로 Error
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError(f"({x}, {y}) is not on the curve")

    def __eq__(self, other: Optional[any]) -> bool:
        return (
            self.x == other.x
            and self.y == other.y
            and self.a == other.a
            and self.b == other.b
        )

    def __ne__(self, other: Optional[any]) -> bool:
        return (
            self.x != other.x
            and self.y != other.y
            and self.a != other.a
            and self.b != other.b
        )

    def __add__(self, other: Optional[any]) -> any:
        # 비교하는 a, b가 둘중에 하나라도 같지 않으면 같은 좌표가 입력되더라도
        # 같은 타원함수 위에 놓여 있지 않으므로 당연히 불가
        if self.a != other.a or self.b != other.b:
            raise TypeError(f"Points {x}, {y} are not on the same curve")

        if self.x is None:
            return other
        if other.x is None:
            return self

        # 해당 함수에서는 y가 다를때는 관계가 없고, x가 같을 때와 다를때가 각기 다른 계산방법으로 정의 된다.
        # 
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = pow(s, 2) - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

        # 두 점이 같고, y좌표가 같으면 무한 원점을 갖는다.
        print(f"{self.y} {self.x} {type(self.y)} {type(self.x)}")
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)

        if self == other:
            # s = (other.y - self.y) / (other.x - self.x)
            s = (3 * pow(self.x, 2) + self.a) / (2 * self.y)
            x = pow(s, 2) - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

    def __rmul__(self, coefficient: int) -> int:
        # 아.. 이런건 쓰지 마세요..
        # product = self.__class__(None, None, self.a, self.b)
        # for _ in range(coefficient):
        #     product += self
        # return product
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result


P = 2**256 - 2**32 - 977


class S256Field(FieldElement):
    def __init__(self, num, prime=None):
        super().__init__(num=num, prime=P)

    def __repr__(self):
        return "{:x}".format(self.num).zfill(64)

    def sqrt(self):
        return self ** ((P + 1) // 4)


A = 0
B = 7

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


class S256Point(Point):
    def __init__(self, x: int, y: int, a: int = None, b: int = None) -> None:
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(x=S256Field(x), y=S256Field(y), a=a, b=b)
        else:
            super().__init__(x=x, y=y, a=a, b=b)

    def __repr__(self):
        if self.x is None:
            return "S256Point(infinity)"
        else:
            return f"S256Point({self.x}, {self.y})"

    def __rmul__(self, coefficient: int):
        coef = coefficient % N
        return super().__rmul__(coef)

    def verify(self, z: int, sig: int):
        s_inv = pow(sig, N - 2, N - 2)
        u = z * s_inv % N
        v = sig.r * s_inv % N
        total = u * G + v * self
        return total.x.num == sig.r

    def sec(self, compressed=True):
        if compressed:
            if self.y.num % 2 == 0:
                return b'\x02' + self.x.num.to_bytes(32, "big")
            else:
                return b'\x03' + self.x.num.to_bytes(32, "big")

        return b'\x04' + self.x.num.to_bytes(32, "big") + self.y.num.to_bytes(32, "big")

    def hash160(self, compressed=True):
        return hash160(self.sec(compressed))

    def address(self, compressed=True, testnet=False):
        h160 = self.hash160(compressed)

        if testnet:
            prefix = b'\x6f'
        else:
            prefix = b'\x00'
        
        return encode_base58_checksum(prefix + h160)

    @classmethod
    def parse(self, sec_bin):
        if sec_bin[0] == 4:
            x = int.from_bytes(sec_bin[1:33], "big")
            y = int.from_bytes(sec_bin[33:65], "big")
            return S256Point(x=x, y=y)

        is_even: bool = sec_bin[0] == 2
        x = S256Field(int.from_bytes(sec_bin[1:]), "big")
        alpha = x ** 3 + S256Field(B)
        beta = alpha.sqrt()

        if beta.num % 2 == 0:
            even_beta = beta
            odd_beta = S256Field(P - beta.num)
        else:
            even_beta = S256Field(P - beta.num)
            odd_beta = beta

        if is_even:
            return S256Point(x, even_beta)
        else:
            return S256Point(x, odd_beta)


G = S256Point(
    0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
)


class Signiture:
    def __init__(self, r, s):
        self.r = r
        self.s = s

    def __repr__(self):
        return f"Signiture({self.r},{self.s})"

    def der(self):
        rbin = self.r.to_bytes(32, "big")
        rbin = rbin.lstrip(b'\x00')

        if rbin[0] & 0x80:
            rbin = b'\x00' + rbin
        
        result = bytes([2, len(rbin)]) + rbin
        
        sbin = self.s.to_bytes(32, "big")
        sbin = sbin.lstrip(b'\x00')

        if sbin[0] & 0x80:
            sbin = b'\x00' + sbin

        result += bytes([2, len(sbin)]) + sbin

        return bytes([0x30, len(result)]) + result


class PrivateKey:
    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G

    def hex(self):
        return f"{self.secret}".zfill(64)

    def sign(self, z):
        k = randint(0, N)
        r = (K * G).x.num
        k_inv = pow(k, N - 2, N)
        s = (z + r * self.secret) * k_inv % N
        if s > N / 2:
            s = N - s
        return Signiture(r, s)

    # https://tools.ietf.org/html/rfc6979
    def deterministic_k(self, z):
        k = b"\x00" * 32
        v = b"\x01" * 32

        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, "big")
        secret_bytes = self.secret.to_bytes(32, "big")
        s256 = hashlib.sha256()
        k = hmac.new(k, v, +b"\x00" + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v, +b"\x01" + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()

        while True:
            v = hmac.new(k, v, s256).digest()
            candidate = int.from_bytes(v, "big")
            if candidate >= 1 and candidate < N:
                return candidate
            k = hmac.new(k, v + b"\x00", s256).digest()
            v = hmac.new(k, v, s256).digest()

    def wif(self, compressed=True, testnet=False):
        secret_bytes = self.secret.to_bytes(32, "big")

        if testnet:
            prefix = b'\xef'
        else:
            prefix = b'\x80'

        if compressed:
            suffix = b'\x01'
        else:
            suffix = b''

        return encode_base58_checksum(prefix + secret_bytes + suffix)