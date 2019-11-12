import math


def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    return 0


class Solution:

    def solve(self, A):

        A = int(A)
        res = A - 1

        num_digits = math.ceil(math.log2(A))

        for m in range(num_digits, 1, -1):

            low, high = 2, A - 1

            while low <= high:

                k = (low + high) >> 1

                left = A * (k - 1)

                # print(k, m)
                right = (k ** m) - 1

                cmp = compare(left, right)

                if cmp == 0:
                    return k
                elif cmp < 0:
                    high = k - 1
                else:
                    low = k + 1
        return res


if __name__ == '__main__':

    S = Solution()
    A = "1000000000000000000"
    print(S.solve(A))