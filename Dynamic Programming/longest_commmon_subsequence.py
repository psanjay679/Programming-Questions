import sys
import random
import string

sys.setrecursionlimit(10000)


def lcs(a, b, i, j):

    global memo

    if i == -1 or j == -1:
        return 0

    if memo[i][j] is None:

        if a[i] == b[j]:
            res = 1 + lcs(a, b, i - 1, j - 1)
        else:
            res = max(lcs(a, b, i, j - 1), lcs(a, b, i - 1, j))
        memo[i][j] = res

    return memo[i][j]


def lcs_start(a, b, i, j):

    global memo

    if i == len(a) or j == len(b):

        memo[i][j] = 0
        return 0

    if memo[i][j] is None:

        if a[i] == b[j]:
            res = 1 + lcs_start(a, b, i + 1, j + 1)
        else:
            res = max(lcs_start(a, b, i + 1, j), lcs_start(a, b, i, j + 1))

        memo[i][j] = res

    return memo[i][j]


a = ''.join(random.choice(string.ascii_letters) for _ in range(1000))
b = ''.join(random.choice(string.ascii_letters) for _ in range(1000))


memo = list()
for i in range(len(a) + 1):
    l = list()
    for j in range(len(b) + 1):
        l.append(None)
    memo.append(l)

print(lcs(a, b, len(a) - 1, len(b) - 1))

memo = list()
for i in range(len(a) + 1):
    l = list()
    for j in range(len(b) + 1):
        l.append(None)
    memo.append(l)

print(lcs_start(a, b, 0, 0))