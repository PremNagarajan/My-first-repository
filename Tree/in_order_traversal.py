class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_traversal(root):
    stack = list()
    curr = root
    while True:
        while curr:
            stack.append(curr)
            curr = curr.left
        if stack:
            curr = stack.pop()
            print curr.data,
            curr = curr.right
        else:
            break
    print


root = TreeNode('a')
root.left = TreeNode('b')
root.left.left = TreeNode('d')
root.left.right = TreeNode('e')
root.right = TreeNode('c')
in_order_traversal(root)