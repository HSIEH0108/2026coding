#week14-2c.py 學習計畫1D DP第一題Easy
#Leetcode 1137. N-th Tribonacci Number
class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
         #函式呼叫函式(不要重複問答案)
        a = [0, 1, 1]
        if n<3: return a[n]
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
