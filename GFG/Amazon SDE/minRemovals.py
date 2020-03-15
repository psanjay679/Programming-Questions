import sys

def findMinRemovals(A):

    minLeft = [float("inf")] * len(A)
    maxLeft = [-float("inf")] * len(A)
    minLeft[-1] = A[-1]
    maxLeft[-1] = A[-1]

    for i in range(len(A) - 2, -1, -1):
        minLeft[i] = min(minLeft[i + 1], A[i])
        maxLeft[i] = max(maxLeft[i + 1], A[i])

    for i in range(len(A)):
        if minLeft[i] * 2 > maxLeft[i]:
            return i

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        A = [int(k) for k in sys.stdin.readline().split()]
        print(findMinRemovals(A))