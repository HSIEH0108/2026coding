#week02-2.py 學習計畫 Two point 第一題
#備用
#LeetCode 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)  #陣列的大小
        k=0
        for i in range(N): #把nums[i]逐一檢查
            if nums[i] != 0: #遇到非0數，要搬到左邊
                nums[k] = nums[i] #左邊nums[k] = nums[i]
                k+=1  #k換到下一個位置
        for i in range(k,N):
            nums[i] = 0
