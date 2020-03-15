from queue import PriorityQueue

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.adj = list()

def dijkstra(graph, start):

    pq = PriorityQueue()
    visited = [False] * len(graph)
    distance = [float('inf')] * len(graph)

    pq.put((0, start))
    distance[start] = 0

    while not pq.empty():

        node, dist = pq.get()

        if visited[node]:
            continue

        for adj in graph[node]:
            distance[adj] = min(adj.dist + distance[node.val], distance[adj.val])
            pq.put((distance[adj.val], adj.val))

