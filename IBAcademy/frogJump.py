import sys
sys. setrecursionlimit(10000)

class Solution:

    def bin_search(self, A, low, high, value):
        while low <= high:
            mid = (low + high) // 2
            if A[mid] < value:
                low = mid + 1
            elif A[mid] > value:
                high = mid - 1
            else:
                return mid

        return -1

    def solve_it(self, A, ind, n, jump):

        if self.memo[n][jump] is None:

            if ind == n:
                self.memo[n][jump] = True
                return True
            if jump == 0:
                self.memo[n][jump] = False
                return False

            res = self.bin_search(A, ind + 1, n, A[ind] + jump)

            result = False

            if res != -1:
                result = self.solve_it(A, res, n, jump - 1)
                result = result or self.solve_it(A, res, n, jump)
                result = result or self.solve_it(A, res, n, jump + 1)
            self.memo[n][jump] = result

        return self.memo[n][jump]

    def solve(self, A):
        self.memo = list()
        for i in range(len(A)):
            self.memo.append([None] * len(A))

        return 1 if self.solve_it(A, 0, len(A) - 1, 1) else 0

if __name__ == '__main__':
    A = [0,1,3,5,6,8,12,17]
    S = Solution()
    print(S.solve(A))