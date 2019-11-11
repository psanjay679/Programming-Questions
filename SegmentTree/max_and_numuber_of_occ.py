class Pair:
    
    def __init__(self, first, second):
        
        self.first = first
        self.second = second


class SegmentTree:
    
    @staticmethod
    def combine(a, b):
        if a.first > b.first:
            return a
        elif b.first > a.first:
            return b
        
        return Pair(a.first, a.second + b.second)
    
    def __init__(self, ar):
        
        self.tree = [Pair(0, 0) for _ in range(len(ar) * 4 + 1)]
        self.ar = ar
        
    def build(self, node, start, end):
        
        if start == end:
            self.tree[node] = Pair(self.ar[start], 1)
        else:
            mid = (end + start) >> 1
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            
            self.tree[node] = SegmentTree.combine(self.tree[2 * node + 1], self.tree[2 * node + 2])
        
    def update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = Pair(value, 1)
        else:
            mid = (start + end) >> 1
            if index < mid:
                self.update(2 * node + 1, start, mid, index, value)
            else:
                self.update(2 * node + 2, mid + 1, end, index, value)

            self.tree[node] = SegmentTree.combine(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def query(self, node, start, end, left ,right):
        
        if left > end or right < start or start > end:
            return Pair(-float('inf'), 0)
    
        if left == start and right == end:
            return self.tree[node]
    
        mid = (start + end) >> 1
        left_ans = self.query(2 * node + 1, start, mid, left, min(right, mid))
        right_ans = self.query(2 * node + 2, mid + 1, end, max(mid + 1, left), right)
        
        return SegmentTree.combine(left_ans, right_ans)