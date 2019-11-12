def gcd(a, b, x, y):

    if a == 0:
        x = 0
        y = 1
        return b

    x1, y1 = None, None

    d = gcd(b % a, a, x1, y1)

    x = y1 - (b // a) * x1
    y = x1

    return d
