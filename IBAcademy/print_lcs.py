memo = list()

def solve(x, y, m, n):

    memo = list()

    for i in range(m + 1):
        memo.append([0] * (n + 1))

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                memo[i][j] = j
            elif j == 0:
                memo[i][j] = i
            elif x[i - 1] == y[j - 1]:
                memo[i][j] = memo[i - 1] [j - 1] + 1
            else:
                memo[i][j] = min(memo[i - 1][j], memo[i][j - 1])
    return memo[i][j]

def main():
    x = "pearafasdf"
    y = "peachfdsafsa"

    # global memo
    # memo = list()
    m = len(x)
    n = len(y)

    # for i in range(m + 1):
    #     memo.append([None] * (n + 1))

    l = solve(x, y, m, n)
    # print(memo)
    # print(m + n - l)
    print(l)
    # ar = [None] * l
    #
    # i, j, ind = m - 1, n - 1, l - 1
    # while i >= 0 and j >= 0:
    #     if x[i] == y[j]:
    #         ar[ind] = x[i]
    #         i -= 1
    #         j -= 1
    #         ind -= 1
    #     elif memo[i][j + 1] > memo[i + 1][j]:
    #         i -= 1
    #     else:
    #         j -= 1
    #
    # print (''.join(ar))

main()