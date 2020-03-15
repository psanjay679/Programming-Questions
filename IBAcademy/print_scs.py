def solve(x, y, m, n):

    global memo

    if memo[m][n] is None:
        if m == 0:
            memo[m][n] = n
            return n
        if n == 0:
            memo[m][n] = m
            return m

        if x[m - 1] == y[n - 1]:
            memo[m][n] = 1 + solve(x, y, m - 1, n - 1)
        else:
            memo[m][n] = 1 + min(
                solve(x, y, m - 1, n),
                solve(x, y, m, n - 1)
            )

    return memo[m][n]

def k():

    x = "algorithm"
    y = "rhythm"

    m = len(x)
    n = len(y)

    global memo

    memo = list()
    for i in range(m + 1):
        memo.append([None] * (n + 1))

    l = solve(x, y, m, n)
    print(l)
    ar = [''] * l

    i, j, ind = m, n, l

    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            ar[ind - 1] = x[i - 1]
            i -= 1
            j -= 1
            ind -= 1
        elif memo[i - 1][j] > memo[i][j - 1]:
            ar[ind - 1] = y[j - 1]
            j -= 1
            ind -= 1
        else:
            ar[ind - 1] = x[i - 1]
            i -= 1
            ind -= 1

    while i > 0:
        ar[ind - 1] = x[i - 1]
        i -= 1
        ind -= 1

    while j > 0:
        ar[ind - 1] = y[j - 1]
        j -= 1
        ind -= 1

    return ''.join(ar)

if __name__ == '__main__':
    main()