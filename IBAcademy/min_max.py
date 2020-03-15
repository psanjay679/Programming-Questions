class Solution:
    def solve(self, A):
        next_greater = list()
        s = list()

        for i, v in enumerate(A):
            if len(s) == 0:
                s.append(i)
            else:
                while len(s) != 0 and A[s[-1]] > v:
                    s.pop()

            
            next_greater.append(s[-1])

        next_greater.append(None)