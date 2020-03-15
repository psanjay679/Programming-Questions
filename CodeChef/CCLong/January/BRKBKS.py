import sys


def find_ans(ar, s):
    ans = 1
    idx = 0
    c_sum = 0

    while idx < len(ar):
        if ar[idx] + c_sum > s:
            c_sum = ar[idx]
            ans += 1
        else:
            c_sum += ar[idx]
        idx += 1
    return ans


def main():

    t = int(sys.stdin.readline())

    for _ in range(t):

        s, *ar = list(map(int, sys.stdin.readline().split()))

        print(min(find_ans(ar, s), find_ans(ar[::-1], s)))


if __name__ == '__main__':
    main()