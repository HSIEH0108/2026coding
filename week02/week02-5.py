#week02-5.py 學習計畫 Two Pointers 第4題 Medium題
#LeetCode 1679. Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()#小到大排好，等一下左邊右邊個挑一個，看能不能組合
        ans=0
        i,j = 0,len(nums)-1
        while i < j:
            if nums[i]+nums[j] == k:
                ans += 1
                i,j = i+1, j-1
            if nums[i]+nums[j] < k: #加起來太小了，左邊小的i要往左移
                i=i+1
            if nums[i] + nums[j] > k: #加起來太大了，右邊大的j要往左移
                j=j-1
        return ans
