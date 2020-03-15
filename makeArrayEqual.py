class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        ma = dict()
        mb = dict()

        cnt = 0
        for i, a in enumerate(A):
            ma[a] = i
        for i, b in enumerate(B):
            mb[b] = i

        for a, b in ma.items():
            if a not in mb:
                cnt += 1

        ans = len(B)
        for a in A:
            if a in mb:
                ans = max(ans, (mb[a] - ma[a] + len(A)) % len(A))

        return min(len(A), ans + cnt)


A = [ 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28 ]
B = [ 65, 28, 66, 64, 35, 169, 25, 1, 100, 36, 79, 46, 15 ]

s = Solution()
print(s.solve(A, B))