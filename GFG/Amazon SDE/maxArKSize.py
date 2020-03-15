import sys
from queue import Queue

if __name__ == '__main__':

    T = int(sys.stdin.readline())
    for _ in range(T):
        n, k = list(map(int, sys.stdin.readline().split()))
        ar = list(map(int, sys.stdin.readline().split()))
        q = Queue()

        for i in range(k):
            while not q.empty() and q[-1][1] < ar[i]:
                q.get()
            q.put((i, ar[i]))
        ans = list()
        ans.append(q[0][1])

        for i in range(k, n):
            while not q.empty() and (q[-1][1] < ar[i] or i - q[-1][0] > k):
                q.get()
            q.put((i, ar[i]))
            ans.append(q[0][1])

        for a in ans:
            print(a, end=" ")
        print()