#week03-2.py 學習計畫 sliding windows
#LeetCode 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums) #陣列長度
        total = sum(nums[:k])#加總 [:k]前K項
        maxTotal = total
        for i in range(k,N): #右邊頭(往右吃),nums[i-k]左邊的尾,吐出來
            total = total + nums[i] - nums[i-k]
            #nums[i]右邊的頭(往右吃),nums[i-k]左邊的尾吐出來
            maxTotal = max(maxTotal,total)#持續更新,找最大的total
        return maxTotal/k #最大平均 = 最大total/k
