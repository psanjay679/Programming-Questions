class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None


def find_height(node):

    if node is None:
        return 0
    
    left_height = find_height(node.left)
    right_height = find_height(node.right)

    return max(left_height, right_height) + 1;

def diameter(root):
    
    if root is None:
        return 0

    left_height = find_height(root.left)
    right_height = find_height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(left_height + right_height + 1, ldiameter, rdiameter)
    



def main():

    root = Node(10)
    root.left = Node(20)
    # root.right = Node(30)
    # root.left.left = Node(40)
    # root.left.right = Node(50)

    diam = diameter(root)
    print (diam)

if __name__ == '__main__':
    main()
    