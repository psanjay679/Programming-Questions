import sys

global memo

def isValid(r, c, N):
    return 0 <= r < N and 0 <= c < N

def findLargestPath(mat, r, c):

    global memo

    if memo[r][c] == -1:
        N = len(mat)
        poss_paths = ((r + 1, c), (r + 1, c + 1), (r + 1, c - 1))
        maxVal = 0
        for x, y in poss_paths:
            if isValid(x, y, N):
                maxVal = max(maxVal, findLargestPath(mat, x, y))
        memo[r][c] = maxVal + mat[r][c]

    return memo[r][c]


if __name__ == '__main__':

    global memo

    T = int(sys.stdin.readline())
    for _ in range(T):

        N = int(sys.stdin.readline())
        memo = list()

        for i in range(N):
            l = [-1] * N
            memo.append(l)

        mat = list()
        ar = list(map(int, sys.stdin.readline().split()))
        for i in range(N):
            m = list()
            for j in range(N):
                m.append(ar[i * N + j])
            mat.append(m)

        ans = 0
        for i in range(N):
            ans = max(ans, findLargestPath(mat, 0, i))

        print(ans)