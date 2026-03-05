#week02-4.py 學習計畫 two pointers
#LeetCode 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i,j = 0,len(height)-1
        while i<j: #只要左右沒撞一起
            area = (j-i)*min(height[i], height[j]) #算出現在的面積
            ans = max(ans,area)#更新答案
            if height[i] < height[j]:i += 1 #小的i，往右
            else: j -= 1 #小的j，往左
        return ans
