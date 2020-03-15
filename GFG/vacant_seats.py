from queue import PriorityQueue
import sys


def main():

    t = int(input())

    for __ in range(t):
        a, b = [int(k) for k in sys.stdin.readline().split()]
        ar = [int(k) for k in sys.stdin.readline().split()]

        pq = PriorityQueue()
        for e in ar:
            pq.put(-e)

        cnt = 0
        for _ in range(b):
            e = -pq.get()
            cnt += e
            e -= 1
            if e > 0:
                pq.put(-e)

        print(cnt)

main()