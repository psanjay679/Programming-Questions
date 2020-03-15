import sys


def find_pairs(a, b, k):

    a.sort()
    b.sort()

    ans = list()
    s = 0
    e = len(b) - 1
    while s < len(a) and e >= 0:
        if a[s] + b[e] > k:
            e -= 1
        elif a[s] + b[e] < k:
            s += 1
        else:
            ans.append((a[s], b[e]))
            s += 1
            e -= 1

    print(', '.join(str(l[0]) + " " + str(l[1]) for l in ans))
    # for _a, _b in ans:
    #     print(_a, _b, end=", ")
    # print()


def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m, k = list(map(int, sys.stdin.readline().split()))
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        find_pairs(a, b, k)


if __name__ == '__main__':
    main()