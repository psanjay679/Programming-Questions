import sys

global parent
global weight


def find(a):
    global parent

    while parent[a] != a:
        a = parent[a]

    return a


def union(a, b):
    global parent
    global weight

    pa = find(a)
    pb = find(b)

    if pa != pb:
        if weight[pa] < weight[pb]:
            parent[pa] = parent[pb]
            weight[pb] += weight[pa]
        else:
            parent[pb] = parent[pa]
            weight[pa] += weight[pb]


def printAns(a, b):
    return "Yes" if find(a) == find(b) else "No"


if __name__ == '__main__':
    N, Q = list(map(int, sys.stdin.readline().split()))
    global parent
    global weight

    parent = [i for i in range(N + 1)]
    weight = [1 for i in range(N + 1)]

    for _ in range(Q):
        a, b, c = list(map(int, sys.stdin.readline().split()))

        if a == 2:
            print(printAns(b, c))
        else:
            union(b, c)
