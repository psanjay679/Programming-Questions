class SegmentTree:
    
    def __init__(self, ar):
        
        self.tree = [0] * (4 * len(ar) + 1)
        self.ar = ar
        self.size = len(ar)
        
        self.build(0, 0, self.size - 1)
        
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.ar[start]
        else:
            mid = (start + end) >> 1
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        
    def update(self, node, start, end, index, value):
        
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) >> 1
            if index < mid:
                self.update(2 * node + 1, start, mid, index, value)
            else:
                self.update(2 * node + 2, mid + 1, end, index, value)
            
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query(self, node, start, end, left, right):
        
        if left > end or right < start or start > end:
            return 0
    
        if left == start and right == end:
            return self.tree[node]
        
        mid = (start + end) >> 1
        return self.query(2 * node + 1, start, mid, left, min(right, mid)) + \
               self.query(2 * node + 1, mid + 1, end, max(left, mid + 1), right)

    def find_first_index(self, node, start, end, total_sum):

        if total_sum > self.tree[node]:
            return -1

        if start == end:
            return start

        mid = (start + end) >> 1

        if self.tree[2 * node + 1] >= total_sum:
            return self.find_first_index(2 * node + 1, start, mid, total_sum)
        else:
            return self.find_first_index(2 * node + 2, mid + 1, end, total_sum - self.tree[2 * node + 1])

    
if __name__ == '__main__':
    pass