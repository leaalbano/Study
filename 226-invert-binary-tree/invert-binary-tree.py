# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #Checks to see if the node is a parent or child
        if not root:
            return None

        #Define what left/ right root is
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        #Inverting process
        root.left = right
        root.right = left

        return root

            
        