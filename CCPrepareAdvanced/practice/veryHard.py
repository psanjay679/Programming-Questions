import sys


global tree


def buildTree(ar, node, k, start, end):
    global tree

    if start == end:
        tree[ar[start] % k][node] += 1
    else:
        mid = (start + end) >> 1
        buildTree(ar, 2 * node + 1, k, start, mid)
        buildTree(ar, 2 * node + 2, k, mid + 1, end)

        for i in range(6):
            tree[i][node] = tree[i][2 * node + 1] + tree[i][2 * node + 2]


def update(ar, node, k, start, end, idx, val):
    global tree

    if start == end:
        tree[ar[idx] % k][node] += val
    else:
        mid = (start + end) >> 1
        if idx < mid:
            update(ar, 2 * node + 1, k, start, mid, idx, val)
        else:
            update(ar, 2 * node + 2, k, mid + 1, end, idx, val)

        # for i in range(6):
        i = ar[idx] % k
        tree[i][node] = tree[i][2 * node + 1] + tree[i][2 * node + 2]


def query(node, start, end, left, right, rem):
    global tree

    if start == end:
        return tree[rem][node]

    if start > right or end < left:
        return 0
    mid = (start + end) >> 1

    return query(2 * node + 1, start, min(mid, end), left, right, rem) + query(2 * node + 2, max(start, mid + 1), end, left, right, rem)


if __name__ == '__main__':

    N, Q, K = list(map(int, sys.stdin.readline().split()))

    ar = list(map(int, sys.stdin.readline().split()))
    global tree

    tree = list()
    for _ in range(6):
        tree.append([0] * (4 * N + 1))

    buildTree(ar, 0, K, 0, N - 1)
    for _ in range(Q):
        q = list(map(int, sys.stdin.readline().split()))
        if q[0] == 1:
            update(ar, 0, K, 0, N - 1, q[1] - 1, -1)
            ar[q[1] - 1] += q[2]
            update(ar, 0, K, 0, N - 1, q[1] - 1, 1)
        else:
            print(query(0, 0, N - 1, q[1] - 1, q[2] - 1, q[3]))