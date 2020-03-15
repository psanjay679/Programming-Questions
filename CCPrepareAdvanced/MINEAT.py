import sys

def isValidK(ar, k, h):
    cnt = 0
    for a in ar:
        if a % k == 0:
            cnt += a // k
        else:
            cnt += a // k + 1
    return cnt <= h

def findMinK(ar, h):
    low = min(ar)
    high = max(ar)
    ans = high

    while low <= high:
        mid = (low + high) >> 1
        is_valid = isValidK(ar, mid, h)
        if is_valid:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

if __name__ == '__main__':

    T = int(sys.stdin.readline())
    for _ in range(T):

        n, h = list(map(int, sys.stdin.readline().split()))
        ar = list(map(int, sys.stdin.readline().split()))
        print(findMinK(ar, h))