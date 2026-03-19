#week04-4b.py 糶week04-3.py
#leetcode 3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0]*200 #
        for nn in nums:
            H[nn] += 1
        for nn in nums: #硋浪琩
            if nn % 2 == 0 and H[nn] == 1: #案计,瞷Ω
                return nn
        return -1
#week04-3.py More Challenges 虏虫肈
#leetcode 3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        ans = -1 #тぃ氮穦琌 -1
        N = len(nums) #ΤN计
        H = [0]*200 #
        for i in range(N):
            H[nums[i]] += 1

        for i in range(N): #硋浪琩
            if nums[i] % 2 == 0 and H[ nums[i] ] == 1: #案计,瞷Ω
                return nums[i]

        return -1
