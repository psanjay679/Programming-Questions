import sys

sys.setrecursionlimit(10000)


def get_count(coins, n, sum):

    global memo

    if memo[sum][n] is None:
        if sum == 0:
            memo[sum][n] = 1
        elif n == 0:
            memo[sum][n] = 0
        else:
            res = get_count(coins, n - 1, sum)
            if coins[n - 1] <= sum:
                res += get_count(coins, n, sum - coins[n - 1])

            memo[sum][n] = res

    return memo[sum][n]


def getCount(coins, n, sum):

    if sum == 0:
        return 1
    if n == 0:
        return 0

    res = get_count(coins, n - 1, sum)

    if coins[n - 1] <= sum:
        res += get_count(coins, n, sum - coins[n - 1])

    return res


coins = [2, 3, 5, 6]
sum = 10000

memo = list()

for i in range(sum + 1):
    l = list()
    for j in range(len(coins)  + 1):
        l.append(None)

    memo.append(l)

print(get_count(coins, len(coins), sum))