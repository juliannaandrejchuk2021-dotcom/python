import math

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b
        self._simplify()

    def _simplify(self):
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

        if self.b < 0:
            self.a *= -1
            self.b *= -1

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __add__(self, other):
        num = self.a * other.b + other.a * self.b
        den = self.b * other.b
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.a * other.b - other.a * self.b
        den = self.b * other.b
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.a * other.a
        den = self.b * other.b
        return Fraction(num, den)

    def __truediv__(self, other):
        if other.a == 0:
            raise ZeroDivisionError("Division by zero fraction")
        num = self.a * other.b
        den = self.b * other.a
        return Fraction(num, den)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print("f1 =", f1)
print("f2 =", f2)

print("f1 + f2 =", f1 + f2)
print("f1 - f2 =", f1 - f2)
print("f1 * f2 =", f1 * f2)
print("f1 / f2 =", f1 / f2)

f3 = Fraction(2, 4)
print("Simplified fraction:", f3)

