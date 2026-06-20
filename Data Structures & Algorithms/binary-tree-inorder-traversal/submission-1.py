# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self) -> None:
        self.values = []
    
    def in_order_search(self, root):
        if not root:
            return None
        
        self.in_order_search(root.left)
        self.values.append(root.val)
        self.in_order_search(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.in_order_search(root)
        return self.values
        
         