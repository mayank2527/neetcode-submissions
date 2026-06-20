# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        items_list = [root]
        level = 0
        while len(items_list) > 0:
            temp_list = []
            level+=1
            while items_list:
                ele = items_list.pop()
                if ele.left:
                    temp_list.append(ele.left)
                if ele.right:
                    temp_list.append(ele.right)

            items_list = temp_list

        return level
