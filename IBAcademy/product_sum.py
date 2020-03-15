def lower_bound(A, val):

    low = 0
    high = len(A)

    ans = 0

    while low < high:
        mid = (low + high) / 2

        if A[mid] <= val:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

class Solution:

    def getSum(self, A, B, C, D, E, F):
