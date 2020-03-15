def find(x):
    global parent

    if parent[x] != -1:
        return x

    x = parent[x]
    return find(x)


def union(a, b):
    global parent

    pa = parent(a)
    pb = parent(b)

    if pa != pb:
        parent[b] = parent[a]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        ar = list(map(int, input().split()))
        