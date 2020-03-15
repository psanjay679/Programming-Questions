class Solution:

    def is_average_poss(self, ar, n, sum1, num1, sum2, num2):

        if n == 0:
            if num1 == 0 or num2 == 0:
                return False

            return sum1 * num1 == sum2 * num1
        else:
            res = self.is_average_poss(ar, n - 1, sum1, num1, sum2, num2)
            res = res or self.is_average_poss(ar, n - 1, sum1 + ar[n - 1], num1 + 1, sum2 - ar[n - 1], num2 - 1)

            return res

    def solve(self, A):
        return self.is_average_poss(A, len(A), 0, 0, sum(A), len(A))

A = [1, 7, 15, 29, 11, 9]
s = Solution()
print(s.solve(A))


# https://www.interviewbit.com/problems/kth-smallest-element-in-a-sorted-matrix/