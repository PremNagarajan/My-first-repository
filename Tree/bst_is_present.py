"""
class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None
"""

def isPresent (root,val):
    # write your code here
    # return 1 or 0 depending on whether the element is present in the tree or not
    if not root:
        return 0
    else:
        if root.value == val:
            return 1
        else:
            return isPresent(root.left, val) or isPresent(root.right, val)