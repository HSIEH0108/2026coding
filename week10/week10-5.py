#week10-5.py學習計畫 Binary Tree - DFS第4題
#LeetCode 437. Path Sum III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#備用
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = Counter()
        counter[0] = 1 #上帝視角的0
        def helper(root,total): #之前的 total
            if root == None:return 0
            total += root.val
            ans = counter[total - targetSum]
            counter[total] += 1 #累積多1個total(的斷點)
            ans += helper(root.left, total)
            ans += helper(root.right, total)
            counter[total] -= 1 #再扣掉
            return ans
        return helper(root,0)
