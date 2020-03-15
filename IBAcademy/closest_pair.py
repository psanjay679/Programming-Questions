class Solution:

    def solve(self, A, B, C):
        i = 0
        j = len(B) - 1

        min_diff = float('inf')
        ans = [0, 0]

        while i < len(A) and j >= 0:
            a = A[i]
            b = B[j]

            if abs(a + b - C) < min_diff:
                ans = [a, b]
                min_diff = abs(a + b - C)
            elif abs(a + b - C) == min_diff:
                if a <= ans[0]:
                    if b < ans[1]:
                        ans = [a, b]
            if a + b > C:
                j -= 1
            else:
                i += 1

        return ans


A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8]
C = 9
S = Solution()
print(S.solve(A, B, C))