import sys

def print_ar(n, ar):

    init = [0] * n
    min_el = 0

    for a in ar:
        if a >= n:
            init = [min_el] * n
        else:
            init[a] -= 1
            min_el = min(min_el, init[a])

    print(' '.join([str(k) for k in init]))


def main():

    t = int(sys.stdin.readline())
    for _ in range(t):
        n, q = [int(k) for k in sys.stdin.readline().split()]
        ar = [int(k) for k in sys.stdin.readline().split()]
        print_ar(n, ar)


if __name__ == "__main__":
    main()