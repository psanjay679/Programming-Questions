import sys


def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        N = int(sys.stdin.readline())
        A = int(sys.stdin.readline())
        S = int(sys.stdin.readline())
        B = int(sys.stdin.readline())
        C = int(sys.stdin.readline())
        D = int(sys.stdin.readline())
        E = int(sys.stdin.readline())
        verdict = int(sys.stdin.readline())

        ans = 1 if A + B + C + D + E == S else -1

        if verdict == -1:
            print(-1)
            break
        else:
            print(verdict)

        sys.stdout.flush()


if __name__ == '__main__':
    main()