import sys
sys.setrecursionlimit(10000)

class Solution:

    def find_ncr(self, n, r):
        if self.memo[n][r] is None:
            if r == 0 or r == n:
                self.memo[n][r] = 1
            else:
                self.memo[n][r] = self.find_ncr(n - 1, r - 1) + self.find_ncr(n - 1, r)
        return self.memo[n][r]

    def solve(self, A, B, C):

        self.memo = list()
        for i in range(A + 1):
            l = [0] * (B + 1)
            self.memo.append(l)

        for i in range(A + 1):
            self.memo[i][0] = 1
        for i in range(B + 1):
            self.memo[i][i] = 1

        for i in range(1, A + 1):
            for j in range(1, B + 1):
                self.memo[i][j] = (self.memo[i - 1][j - 1] + self.memo[i - 1][j]) % C

        return self.memo[A][B] % C

A = 3878
B = 254
C = 3406

S = Solution()
print(S.solve(A, B, C))