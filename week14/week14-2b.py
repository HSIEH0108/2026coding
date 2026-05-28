#week14-2b.py 學習計畫1D DP第一題Easy
#Leetcode 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        @cache #函式呼叫函式(不要重複問答案)
        def helper(i):
            if i == 0:return 0
            if i == 1:return 1
            if i == 2:return 1
            return helper(i-1) + helper(i-2) + helper(i-3)
        return helper(n)
