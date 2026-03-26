#week05-2c.py 學習計畫 Hash Table (Map/Set)
#LeetCode 2215. Find the Difference of Two Arrays
#備用
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1,nums2=set(nums1),set(nums2) #只加這行第2版本
        return [list(nums1 - nums2), list(nums2-nums1)]
