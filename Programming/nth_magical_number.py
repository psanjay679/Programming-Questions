import math


def gcd(a, b):

    if a % b == 0:
        return b
    if b % a == 0:
        return a

    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


class Solution:

    def solve(self, N, A, B):

        if A > B:
            return self.solve(N, B, A)

        if B % A == 0:
            return (A * N) % (1e9 + 7)

        low = A
        high = A * N
        lcm = A // gcd(A, B) * B

        while low <= high:

            mid = (high + low) >> 1

            c = mid // A + mid // B - mid // lcm

            if c < N:
                low = mid + 1
            else:
                high = mid - 1

        return int(low % (1e9 + 7))


if __name__ == '__main__':

    N, A, B = 807414236, 3788, 38141
    S = Solution()
    print(S.solve(N, A, B))