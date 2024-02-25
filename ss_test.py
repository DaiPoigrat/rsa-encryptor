from random import randint
from math import gcd


def jacoby(a: int, n: int):
    if n <= 0 or n % 2 == 0:
        return -1

    a = a % n
    t = 1

    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t

        a, n = n, a

        if a % 4 == n % 4 == 3:
            t = -t

        a = a % n

    if n == 1:
        return t
    return 0


def is_simple(n: int, k: int):
    if n < 2:
        return False
    for i in range(k):
        a = randint(2, n - 1)

        if gcd(a, n) > 1:
            return False

        else:
            r = jacoby(a, n)
            if r == -1:
                return False
            power = int((n - 1) / 2)
            s = pow(a, power, n)
            if r != s:
                return False

    return True


if __name__ == '__main__':
    print(f'{pow(5, 9, 19) = }')
