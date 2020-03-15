import sys

global memo

def coinChange(ar, s):

    memo = [float("inf")] * (s + 1)
    memo[0] = 0

    for i in range(s + 1):
        for j in range(len(ar)):
            if i - ar[j] >= 0:
                sub_res = memo[i - ar[j]]
                if sub_res != float("inf") and memo[i] > sub_res + 1:
                    memo[i] = 1 + sub_res
    return memo[s]

if __name__ == '__main__':

    global memo

    T = int(sys.stdin.readline())
    for _ in range(T):
        S, N = list(map(int, sys.stdin.readline().split()))
        A = list(map(int, sys.stdin.readline().split()))
        memo = [float("inf")] * (S + 1)
        print (coinChange(A, S))