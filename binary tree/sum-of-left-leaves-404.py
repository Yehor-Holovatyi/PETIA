# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        total = 0 
        # appleі on a branch

        if root.left:
            if not root.left.left and not root.left.right:
                # an apple without a meaning that will have a meaning
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        total += self.sumOfLeftLeaves(root.right)

        return total
        
