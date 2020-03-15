def isRoundRotation(a, b):
    n = len(a)
    m = len(b)

    lps = [0] * n
    i = 0
    l = 0

    while i < n:
        if a[i] == b[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l == 0:
                lps[i] = 0
                i += 1
            else:
                l = lps[l - 1]
    i = 0

    for k in range(lps[n - 1], m):
        if b[k] != a[i]:
            return False
        else:
            i += 1