def find_mid(start, end):
    
    return (start + end) >> 1


class SegmentTree:
    
    def __init__(self, ar):
        
        self.size = len(ar)
        self.tree = [0] * (4 * self.size + 1)
        self.ar = ar
        
        self.build(0, 0, self.size - 1)
        
    def build(self, node, start, end):
        
        if start == end:
            if self.ar[start] == 0:
                self.tree[node] = 1
        else:
            mid = find_mid(start, end)
            
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        
    def update(self, node, start, end, index, value):
        
        if start == end:
            if self.ar[index] == 0:
                self.tree[node] = 1
            else:
                self.tree[node] = 0
        else:
            mid = find_mid(start, end)
            
            if mid < index:
                self.update(2 * node + 1, start, mid, index, value)
            else:
                self.update(2 * node + 2, mid + 1, end, index, value)
            
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
            
    def query(self, node, start, end, left, right):
        
        if start > end or start > right or end < left:
            return 0
    
        if start == left and right == end:
            return self.tree[node]
    
        mid = find_mid(start, end)
        
        return self.query(2 * node + 1, start, mid, left, min(right, mid)) + \
            self.query(2 * node + 2, mid + 1, end, max(mid + 1, left), right)