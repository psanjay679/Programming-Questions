class Solution:

    def max_sum_subarray(self, ar):

        dp = [0] * len(ar)
        dp[0] = ar[0]

        max_sum = dp[0]

        for i in range(1, len(ar)):
            dp[i] = max(dp[i - 1] + ar[i], ar[i])
            max_sum = max(max_sum, dp[i])

        return max_sum

    def solve(self, A):
        for i in range(len(A)):
            A[i] = [0] + A[i]

        for i in range(len(A)):
            for j in range(1, len(A[i])):
                A[i][j] += A[i][j - 1]

        max_sum = 0
        for s in range(len(A[0]) - 1):
            for e in range(s + 1, len(A[0])):
                ar = [0] * len(A)
                for i in range(len(ar)):
                    ar[i] = A[i][e] - A[i][s]

                max_sum = max(self.max_sum_subarray(ar), max_sum)

        return max_sum

A = [   [1, 3, -2],
            [1, 4, 6],
            [-4, -2, 1]   ]

s = Solution()
print(s.solve(A))