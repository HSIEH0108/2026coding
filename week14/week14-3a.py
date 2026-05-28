#week14-3a.py 學習計畫1D DP第一題Easy
#Leetcode 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache #函式呼叫函式，把大問題拆成小問題
        def helper(i): #現在踩在第i格，之前要多少錢?
            if i >= len(cost):return 0 #終止條件
            return cost[i] + min(helper(i+1),helper(i+2))
        return min(helper(0),helper(1))
