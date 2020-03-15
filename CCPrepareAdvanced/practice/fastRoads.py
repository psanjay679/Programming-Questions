import sys
from queue import PriorityQueue


def dijkstra(adj, V, src, dst):

    visited = [False] * (V + 1)
    dist = [float("inf")] * (V + 1)
    pq = PriorityQueue()
    pq.put((0.0, src))
    dist[src] = 0

    while not pq.empty():
        u = pq.get()[1]
        if not visited[u]:
            visited[u] = True
            for v, w in adj[u]:
                dist[v] = min(dist[v], dist[u] + w)
                pq.put((dist[v], v))

    if dist[dst] == float('inf'):
        return - 1
    else:
        return "%.8f" % dist[dst]


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, u, v = list(map(int, sys.stdin.readline().split()))
        adj = list()
        for i in range(N + 1):
            adj.append(list())

        for _ in range(M):
            x, y, l, s = list(map(int, sys.stdin.readline().split()))
            adj[x].append((y, float(l) / float(s)))
            adj[y].append((x, float(l) / float(s)))

        print(dijkstra(adj, N, u, v))


if __name__ == "__main__":
    main()