import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildBST(ar, l, r):

    if l <= r:
        m = (l + r) >> 1
        node = Node(ar[m])
        node.left = buildBST(ar, l, m - 1)
        node.right = buildBST(ar, m + 1, r)
        return node

    return None


def printPreorder(bst):

    if bst is not None:
        print(bst.val, end=" ")
        printPreorder(bst.left)
        printPreorder(bst.right)


def findBBST(ar):
    l = 0
    h = len(ar) - 1
    bst = buildBST(ar, l, h)
    printPreorder(bst)
    print()

if __name__ == '__main__':

    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        ar = [int(k) for k in sys.stdin.readline().split()]
        findBBST(ar)