# week04-4c.py 重寫week04-4b.py
# leetcode 3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = Counter(nums) #很多很多
        for nn in nums: #逐一檢查
            if nn % 2 == 0 and H[nn] == 1: #偶數,只出現一次
                return nn
        return -1
