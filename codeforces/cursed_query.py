import sys


def find(ar, val):

    low = 0
    high = len(ar) - 1
    ans = -1

    while low <= high:
        mid = (low + high) >> 1
        if ar[mid] < val:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1

    return ans + 1


def main():

    n, k = [int(k) for k in sys.stdin.readline().split()]
    ar = [int(k) for k in sys.stdin.readline().split()]
    prefix_sum = [0] * n
    prefix_sum[0] = ar[0] - 1
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + ar[i]

    for _ in range(k):
        q = int(sys.stdin.readline())
        q = q % (prefix_sum[-1] + 1)
        print(find(prefix_sum, q))


if __name__ == '__main__':
    main()