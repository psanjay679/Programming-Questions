import sys
global ans


def is_valid(adj, x, y, N, M):

    return 0 <= x < N and 0 <= y < M and adj[x][y]


def get_pairs(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]


def find_largest_util(x, y, N, M):

    global adj
    global ans

    pairs = get_pairs(x, y)
    for a, b in pairs:
        if is_valid(adj, a, b, N, M):
            ans += 1
            adj[a][b] = 0
            find_largest_util(a, b, N, M)


def find_largest(N, M):
    global adj
    global ans
    maxVal = 0
    for i in range(N):
        for j in range(M):
            if adj[i][j]:
                ans = 0
                find_largest_util(i, j, N, M)
                maxVal = max(ans, maxVal)
    return maxVal


if __name__ == '__main__':

    t = int(sys.stdin.readline())
    global adj

    for _ in range(t):
        n, m = list(map(int, sys.stdin.readline().split()))
        adj = list()
        ar = list(map(int, sys.stdin.readline().split()))
        for i in range(n):
            adj.append(ar[i * m:(i  + 1)* m])

        print(find_largest(n, m))