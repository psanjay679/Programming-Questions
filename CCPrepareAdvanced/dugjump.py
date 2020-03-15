import sys
from queue import SimpleQueue

def main():

    s = [int(k) for k in list(sys.stdin.readline().strip())]

    V = list()

    for i in range(10):
        V.append(list())

    for i in range(1, len(s)):
        V[s[i]].append(i)

    visited = [False] * (len(s) + 1)
    dist = [False] * len(s)

    q = SimpleQueue()
    q.put(0)
    visited[0] = True
    dist[0] = 0

    while not q.empty():
        idx = q.get()
        if idx == len(s) - 1:
            break

        val = s[idx]

        for nidx in V[val]:
            if visited[nidx] is False:
                dist[nidx] = dist[idx] + 1
                visited[nidx] = True
                q.put(nidx)

        if idx - 1 >= 0 and visited[idx] is False:
            visited[idx - 1] = True
            q.put(idx - 1)
            dist[idx - 1] = dist[idx] + 1

        if idx + 1 < len(s) and visited[idx + 1] is False:
            visited[idx + 1] = True
            q.put(idx + 1)
            dist[idx + 1] = dist[idx] + 1

    print (dist[len(s) - 1])

if __name__ == '__main__':
    main()
