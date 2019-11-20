from math import sqrt
# This module was written by Dmitry Shirshov, with whom we helped to our roomate, so I decided we can use this module
# there, although it's not written by one of us.


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(
            self.x + other.x,
            self.y + other.y
        )

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(
            self.x - other.x,
            self.y - other.y
        )

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector2D(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        else:
            raise ValueError("Я не умею умножать {0} с {1}".format(self, other))

    def __rmul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector2D(
                self.x * other,
                self.y * other
            )
        else:
            raise ValueError("Я не умею умножать {0} и {1}".format(self, other))

    def __eq__(self, other):
        if self is other:
            return True
        return self.x == other.x and self.y == other.y

    def __imul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            self.x *= other
            self.y *= other
            return self
        else:
            raise ValueError("Я не умею домножать {0} на {1}".format(self, other))

    def __truediv__(self, other):
        if (isinstance(other, float) or isinstance(other, int)) and other != 0:
            return Vector2D(
                self.x / other,
                self.y / other
            )
        else:
            raise ValueError("Я не умею делить {0} на {1}".format(self, other))

    def __itruediv__(self, other):
        if (isinstance(other, float) or isinstance(other, int)) and other != 0:
            self.x /= other
            self.y /= other
            return self
        else:
            raise ValueError("Я не умею делить {0} на {1}".format(self, other))

    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def copy(self):
        return Vector2D(self.x, self.y)

    def __str__(self):
        return "Vector {{x = {0}, y = {1}}}".format(self.x, self.y)


if __name__ == "__main__":
    v1 = Vector2D(1, 1)
    v1 /= 0.5
    print(v1)
