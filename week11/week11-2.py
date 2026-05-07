# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#week11-2.py 學習計畫 Binary Tree 最後一題
#LeetCode 236. Lowest Common Ancestor of a Binary Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = []
        def helper(root):
            count = 0 #請問下面累積幾個p或q的node
            if root == None:return 0
            if root == p or root == q : count += 1
            count += helper(root.left)
            count += helper(root.right)
            if count == 2: #收集齊2個，太好了
                a.append(root)
            return count
        helper(root)
        return a[0]
