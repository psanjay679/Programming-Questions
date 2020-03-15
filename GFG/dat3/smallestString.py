# from sets import Set as set
from collections import deque
import sys

ans = ""
my_set = set([])
q = deque([])
N = 0


def rotate(s, R):
    global ans, my_set, q
    s = s + s
    idx = N - R
    # print("appended" ,s)
    while idx > 0 and R > 0:
        str = s[idx: idx + N]
        # print(str)
        if str not in my_set:
            ans = min(ans, str)
            my_set.add(str)
            q.append(str)
        idx -= R


def add(s):
    global ans, my_set, q

    for i in range(1, 10):
        str = ""
        for j in range(0, N):
            if j % 2 == 0:
                str += s[j]
            else:
                if s[j] == '0':
                    str += '1'
                else:
                    str += '0'
                # str += chr((int(s[j]) + i * A) % 10 + 48)
        if str not in my_set:
            ans = min(ans, str)
            my_set.add(str)
            q.append(str)


def bfs(s, R):
    global ans, my_set, q, N
    ans = s
    my_set.clear()
    my_set.add(s)
    q.clear()
    q.append(s)
    N = len(s)
    while q:
        s = q.popleft()
        add(s)
        rotate(s, R)


'''def SmallestString(self, s, R, A):
    R = R % len(s)
    A = A % 10
    bfs(s, R, A)
    return ans'''


class Solution:
    def SmallestString(self, s, R):
        if (len(s) != 0):
            R = R % len(s)
        bfs(s, R)
        return ans

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    sol = Solution()
    for _ in range(t):
        s, r = sys.stdin.readline().split()
        r = int(r)
        s = s.strip()
        print(int(sol.SmallestString(s, r), 2))
