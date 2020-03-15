class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        s = list()

        for i in range(len(A) - 1, -1, -1):
            if A[i] == ']':
                s.append(A[i])
            elif A[i] == '[':
                top = s[-1]
                s.pop()
                _s = ''
                while top != ']':
                    _s += top
                    top = s[-1]
                    s.pop()
                s.append(_s)

            elif A[i].isdigit():
                s[-1] = s[-1] * int(A[i])
            else:
                if len(s) == 0 or s[-1] == ']':
                    s.append(A[i])
                else:
                    s[-1] = A[i] + s[-1]

        ans = ''
        while len(s):
            ans = ans + s[-1]
            s.pop()

        return ans

#
# A = "3[a]2[bc]"
# ans = "aaabcbc"
#
# print (Solution().solve(A))
#
# A = "3[a2[c]]"
# ans = "accaccacc"
#
# print (Solution().solve(A))

A = "2[abc]3[cd]ef"
ans = "abcabccdcdcdef"

print (Solution().solve(A) == ans)