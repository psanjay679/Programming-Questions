class Solution:

    def solve(self, A):

        w_ar = [0] * len(A)
        w_ar[-1] = 1 if A[-1] == 'w' else 0

        for i in range(len(A) - 2, -1, -1):
            w_ar[i] = w_ar[i + 1]

            if A[i] == 'w':
                w_ar[i] += 1
        o_ar = [0] * len(A)

        if A[0] == 'o':
            o_ar[0] = 1

        for i in range(1, len(A)):
            o_ar[i] = o_ar[i - 1]
            if A[i] == 'o':
                o_ar[i] += 1

        ow_ar = [0] * len(A)

        for i in range(len(A) - 1):
            ow_ar[i] = o_ar[i] * w_ar[i + 1]

        v_ar = [0] * len(A)
        if A[0] == 'v':
            v_ar[0] = 1

        for i in range(1, len(A)):
            v_ar[i] = v_ar[i - 1]
            if A[i] == 'v':
                v_ar[i] += 1

        vow_ar = [0] * len(A)

        for i in range(len(A) - 1):
            vow_ar[i] = vow_ar[i - 1] + v_ar[i] * ow_ar[i + 1]

        return vow_ar[-2]


ar = "ovvwo"
s = Solution()
print(s.solve(ar))
