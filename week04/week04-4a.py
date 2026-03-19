#week04-4a.py(重寫week04-2.py)
#學習計畫 Prefix sum 地1題
#1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0 #一開始高度是0
        for gg in gain:
            H += gg #現在增減量是gain[i]加進H
            ans = max(ans,H)#更新最高的答案
        return ans

# week04-2.py 學習計畫 Prefix sum 地1題
# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain) #陣列的長度N
        ans = H = 0 #一開始高度是0
        for i in range(N):
            H += gain[i] #現在增減量是gain[i]加進H
            ans = max(ans,H)#更新最高的答案
        return ans
