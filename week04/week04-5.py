#week04-5 學習計畫 prefix sum 地2題
#LeetCode 724. Find Pivot Index
#備用
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0]
        for i in range (N):
            prefix.append(prefix[-1] + nums[i])#陣列便長
        postfix = [0]*(N+1)
        for i in range(N-1,-1,-1): #倒過來迴圈
            postfix[i]=postfix[i+1] + nums[i]
        for i in range(N):
            if prefix[i] == postfix[i+1]:return i
        return -1
