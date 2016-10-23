"""

226. Invert Binary Tree

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution(object):
    def level_order(self, root):
        if root is None:
            return
        
        queue = list()
        queue.append(root)
        
        while len(queue) > 0:
            queue = queue[::-1]
            node = queue.pop()
            print node.val
            queue = queue[::-1]
            
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or (root.left is None and root.right is None):
            return root
        else:
            temp = root.right
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(temp)
            return root
            
#        1
#    2       3
# 4              5
#
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
s = Solution()
s.level_order(root)
print
root = s.invertTree(root)
s.level_order(root)