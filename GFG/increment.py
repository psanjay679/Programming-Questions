from queue import PriorityQueue

def update_ar(ar):

    ans = [None] * len(ar)

    dq_map = dict()

    for i, a in enumerate(ar):
        if a not in dq_map:
            dq_map[a] = PriorityQueue()
            dq_map[a].put(i)
        else:
            e = dq_map[a].get()

            if dq_map[a].empty():
                del dq_map[a]
            ans[e] += 1

            if ans[e] in dq_map:
                dq_map[ans[e]].put(e)
            else:
                dq_map[ans[e]] = PriorityQueue()
                dq_map[ans[e]].put(e)

        if a not in dq_map:
            dq_map[a] = PriorityQueue()
            dq_map[a].put(i)
        ans[i] = a
    return ans


if __name__ == '__main__':
    import sys
    t = int(input())

    for _ in range(t):
        n = int(input())
        ar = [int(k) for k in sys.stdin.readline().split()]
        ar = update_ar(ar)
        for a in ar:
            print(a, end=" ")

        print()
