"""

The Directrix here is y = 0 and focus is (A,B). all you need to do is apply distance formula for focus: y2 = (x-A)2 + (x-B)2 this simplify to 2by = 1x2 -2ax + a2 + b2 On comparing this gives: M = 2b N = 1 O = -2a P = a2 + b2

"""

class Solution:

    def solve(self, A, B):
        M = 2 * B
        N = 1
        O = -1 * 2 * A
        P = A * A + B * B

        return [M, N, O, P]

