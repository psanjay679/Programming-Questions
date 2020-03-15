from queue import Queue

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers

    def BFS(self, adj, vals):

        visited = [False] * (len(vals) + 1)
        matrixAdj = dict()

        Q = Queue()
        Q.put((1, 0))
        Q.put(None)

        while not Q.empty():
            node = Q.get()
            if node:
                while node:
                    node, level = node
                    visited[node] = True
                    for _node in adj[node]:
                        if not visited[_node]:
                            Q.put((_node, level + 1))

                    if node not in matrixAdj:
                        matrixAdj[level] = list()

                    matrixAdj[level].append(vals[node - 1])
                    node = Q.get()
                Q.put(None)

        for key, value in matrixAdj.items():
            matrixAdj[key] = sorted(matrixAdj[key])

        return matrixAdj

    def binSearch(self, a, v):
        low = 0
        high = len(a) - 1
        ans = -1
        while low <= high:
            mid = (low + high) >> 1
            if a[mid] >= v:
                ans = a[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def solve(self, A, B, C, D, E, F):
        adj = dict()
        for b, c in zip(B, C):
            if b not in adj:
                adj[b] = []
            adj[b].append(c)

            if c not in adj:
                adj[c] = []
            adj[c].append(b)

        matrixAdj = self.BFS(adj, D)
        ans = list()
        # print(matrixAdj)
        max_level = max(matrixAdj.keys())
        for l, x in zip(E, F):
            ans.append(self.binSearch(matrixAdj[l % (max_level + 1) ], x))

        return ans


A = [5]
B = [1, 4, 3, 1]
C = [5, 2, 4, 4]
D = [7, 38, 27, 37, 1]
E = [1, 1, 2]
F = [32, 18, 26]
s = Solution()
print(s.solve(A, B, C, D, E, F))
