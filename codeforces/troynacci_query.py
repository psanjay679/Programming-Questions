import sys


def main():
    md = 10 ** 9 + 7

    n, q = [int(k) for k in sys.stdin.readline().split()]
    fib = [0] * n
    fib[0], fib[1] = [int(k) for k in sys.stdin.readline().split()]
    a, b = [int(k) for k in sys.stdin.readline().split()]
    for i in range(2, n):
        fib[i] = (b * fib[i - 1] + a * fib[i - 2]) % md

    ar = [int(k) for k in sys.stdin.readline().split()]

    for _ in range(q):
        l, r = [int(k) for k in sys.stdin.readline().split()]

        for i in range(l - 1, r):
            ar[i] = (ar[i] + fib[i - l + 1]) % md

    print(' '.join([str(k) for k in ar]))


if __name__ == '__main__':
    main()