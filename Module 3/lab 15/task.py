import math
class Vector3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        return f"Vector3D({self.x},{self.y},{self.z})"

    def __add__(self,other):
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
            )
    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
    def __sub__(self, other):
        return Vector3D(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(
                self.x * other,
                self.y * other,
                self.z * other
            )
        elif isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Unsupported operand type")

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            self.z *= other
            return self
        else:
            raise TypeError("Only scalar multiplication is allowed")

    def __truediv__(self, number):
        if number == 0:
            raise ZeroDivisionError("Division by zero")
        return Vector3D(
            self.x / number,
            self.y / number,
            self.z / number
        )

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __ne__(self, other):
        return abs(self) != abs(other)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1:", v1)
print("v2:", v2)

print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("-v1 =", -v1)

print("v1 * 3 =", v1 * 3)
print("v2 / 2 =", v2 / 2)

print("Scalar product v1 * v2 =", v1 * v2)

print("|v1| =", abs(v1))
print("|v2| =", abs(v2))

print("v1 == v2:", v1 == v2)
print("v1 < v2:", v1 < v2)
print("v1 > v2:", v1 > v2)

v1 += v2
print("v1 after += v2:", v1)

v2 *= 2
print("v2 after *= 2:", v2)