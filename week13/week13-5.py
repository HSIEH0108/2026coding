# week13-4.py 學習計畫 Heap / Priority Queue 第3題
#Leetcode 2542. Maximum Subsequence Score
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        N = len(nums1) # 陣列的長度
        a = [(nums2[i], nums1[i]) for i in range(N)] # 左右合一
        #print(a)
        #a.sort() # 試試看：小到大排好
        #print(a)
        a.sort(reverse=True) # 大到小排好

        heap = [a[i][1] for i in range(k)] # 找到最前面的 k 組數字中的 nums2
        heapify(heap) # 之後將小到大依序吐掉 nums1 的這 k 個數，換...
        total = sum(heap)
        ans = total * a[k-1][0] # 前 k 項的 nums1 及對應最小的 num2 乘積之和？
