import sys

global memo

def editDistance(a, b, n, m):

    global memo

    if memo[n][m] == -1:

        if n == 0:
            return m
        if m == 0:
            return n
        if a[n - 1] == b[m - 1]:
            memo[n][m] = editDistance(a, b, n - 1, m - 1)
        else:
            memo[n][m] = 1 + min(
                editDistance(a, b, n - 1, m),
                editDistance(a, b, n, m - 1),
                editDistance(a, b, n - 1, m - 1)
            )

    return memo[n][m]

if __name__ == '__main__':
    global memo

    T = int(sys.stdin.readline())
    for _ in range(T):

        memo = list()

        n, m = list(map(int, sys.stdin.readline().split()))

        for i in range(n + 1):
            l = [-1] * (m + 1)
            memo.append(l)

        a, b = sys.stdin.readline().split()

        print (editDistance(a, b, n, m))