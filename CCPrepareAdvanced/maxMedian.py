class Solution:
    # @param A : list of integers
    # @param B : string
    # @return a strings

    def is_valid(self, ar, m, k):
        for v in ar[len(ar)//2:]:
            if v >= m:
                return True

            k -= m - v
            if k < 0: return False

        return True

    def solve(self, A, B):
        k = int(B)
        low = A[len(A)//2]
        ans = low
        high = low + k

        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(A, mid, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return str(ans)

if __name__ == '__main__':

    A = [2, 2, 3, 3, 5, 6, 6, 7, 8, 9, 12, 13, 15, 17, 18, 19, 19]
    B = "46"
    s = Solution()
    print(s.solve(A, B))