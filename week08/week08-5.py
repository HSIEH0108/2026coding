#week08-5.py學習計畫 Binary Search 第3題
#LeetCode 162. Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 笨方法：for 迴圈不行嗎？（因為老師發現，這題只有 1000 個數）
        N = len(nums) # 陣列大小 N

        # i:0 最大（只有 1 個數，就是最大。別再 nums[i-1] nums[i+1] 了啦）
        if N == 1: return 0

        for i in range(N): # 每個 index i 都去試左邊、右邊
            if i == 0: # 沒有左邊，只測右邊（要比右邊大）
                if nums[i] > nums[i+1]:
                    return i

            elif i == N-1: # 最右邊、沒有右邊，只測左邊（要比左邊大）
                if nums[i] > nums[i-1]:
                    return i

            # 下面可能會當機，因 i-1 或 i+1 會超過範圍。所以加上面的 if
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

        # 這題其實希望你用 Binary Search，但目前測項測試力有限，for 迴圈也可解
