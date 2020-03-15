import sys


def find_cnt(s, m, indx, n):
    if n == 0:
        return 1 if int(''.join(s), 2) % m == 0 else 0
    else:
        s[indx[n - 1]] = '1'
        cnt = find_cnt(s, m, indx, n - 1)
        s[indx[n - 1]] = '0'
        cnt += find_cnt(s, m, indx, n - 1)
        return cnt


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):

        n, m = list(map(int, sys.stdin.readline().split()))
        s = list(sys.stdin.readline().strip())
        indx = list()
        for i in range(n):
            if s[i] == '_':
                indx.append(i)

        print(find_cnt(s, m, indx, len(indx)))
