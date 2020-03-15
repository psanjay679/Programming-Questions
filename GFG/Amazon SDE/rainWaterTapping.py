import sys

def findMaxWater(A):
    l = 0
    h = len(A) - 1
    maxLeft = A[l]
    maxRight = A[h]
    ans = 0
    while l <= h:
        if A[l] < A[h]:
            if maxLeft < A[l]:
                maxLeft = A[l]
            else:
                ans += maxLeft - A[l]
            l += 1
        else:
            if maxRight < A[h]:
                maxRight = A[h]
            else:
                ans += maxRight - A[h]
            h -= 1
    return ans

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        A = [int(k) for k in sys.stdin.readline().split()]
        print(findMaxWater(A))