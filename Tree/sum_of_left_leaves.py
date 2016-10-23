"""

404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafHelper(self, root, isLeft):
        if root is None:
            return 0
        elif root.left is None and root.right is None and isLeft:
            return root.val
        elif root.left is None:
            return 0 + self.leafHelper(root.right, False)
        elif root.right is None:
            return 0 + self.leafHelper(root.left, True)
        else:
            return 0 + self.leafHelper(root.left, True) + self.leafHelper(root.right, False)
            
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.leafHelper(root, False)
        
#        1
#    2       3
# 4        5
#
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
s = Solution()
print s.sumOfLeftLeaves(root)