# week01-4.py 學習計畫 Array/string 第3題
# leetcode 1431. Kids With the Greatest Number of Candies
# 你給額外的extraCandy後，小朋友手上糖果，會是最多嗎
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

    #(請庫存、救命用)只要Test Result 有綠色 Accept就好
        ans = []
        best = max(candies)
        for candie in candies: #逐一檢查，如果把extraCandies給小朋友
            if candie + extraCandies >= best:ans.append(True)
            else: ans.append(False) #他會不會 >= 最多的，依序塞入 ans
        return ans
