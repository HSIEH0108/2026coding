#week08-4.py 學習計畫 Binary Search 第2題
#LeetCode 2300. Successful Pairs of Spells and Potions
#備用
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        p = len(potions)
        ans = []
        for spell in spells: #每一種魔法，都試一次
            now = p - bisect_left(potions,success/spell)
            ans.append(now)
        return ans
