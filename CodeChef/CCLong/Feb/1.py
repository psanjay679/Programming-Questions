import sys

t = int(sys.stdin.readline())

for _ in range(t):
    __ = int(sys.stdin.readline())
    a = sorted([int(k) for k in sys.stdin.readline().split()])
    b = sorted([int(k) for k in sys.stdin.readline().split()])

    print (sum([min(_a, _b) for _a, _b in zip(a, b)]))