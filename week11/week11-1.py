#week11-1.py 學習計畫Binary Tree - DFS 第2題easy題
#LeetCode 872. Leaf-Similar Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []
        def helper(root):
            if root.left == None and root.right == None: #葉子
                a.append(root.val)
            if root.left: helper(root.left) #如果有左邊
            if root.right: helper(root.right) #如果有右邊
        helper(root1)
        a,b = [], a
        helper(root2)
        print('a',a)
        print('b',b)
        return a == b
