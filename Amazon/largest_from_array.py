import sys
import functools


def compare(a, b):

    a = str(a)
    b = str(b)

    return int(a + b) - int(b + a)


if __name__ == '__main__':
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        ar = list(map(int, sys.stdin.readline().split()))
        ar = sorted(ar, key=functools.cmp_to_key(compare))
        ar = ar[::-1]
        print (''.join(str(k) for k in ar))
        # print(ar)