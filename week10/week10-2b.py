#week10-2b.py 學習計畫 binary Search tree 第1題
#LeetCode 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0 #沒有東西，深度是0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
