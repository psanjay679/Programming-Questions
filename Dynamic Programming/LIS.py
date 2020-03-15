def lis(ar, start, n, val):

    if start == n:
        return 0

    if ar[start] > val:
        res = max(1 + lis(ar, start + 1, n, ar[start]), lis(ar, start + 1, n, val))
    else:
        res = max(lis(ar, start + 1, n, val), lis(ar, start + 1, n, ar[start]))

    return res

memo = [0] * (n + 1)
ar = [4, 10, 6, 5, 8, 11, 2, 20]
start = 0
ar = [10, 5, 18, 7, 2, 9]
n = len(ar)
val = float("-inf")
print(lis(ar, start, n, val))
