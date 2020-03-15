
class Solution:

    def min_sum_diff(self, ar, n, sc, st):

        if n == 0:
            return abs((st - sc) - sc)

        if self.memo[n][sc] is None:
            self.memo[n][sc] = min(
                self.min_sum_diff(ar, n - 1, sc, st),
                self.min_sum_diff(ar, n - 1, sc + ar[n - 1], st)
            )

        return self.memo[n][sc]

    def solve(self, A):

        memo = list()
        st = sum(A)

        for i in range(len(A) + 1):
            memo.append([None] * (sum(A) + 1))

        self.memo = memo

        min_diff = self.min_sum_diff(A, len(A), 0, st)

        ans = (st + min_diff) * (st - min_diff)
        ans = ans / 4

        return ans