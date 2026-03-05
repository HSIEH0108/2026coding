#week02-3.py 學習計畫 Two Pointers 第2題
#LeetCode 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1,N2 = len(s),len(t) #字串的長度
        if N1==0: return True
        i = 0
        for k in range(N2): #右邊一個個去試
            if s[i] == t[k]: #找到一個做又符合的
                i += 1 #左邊的i往右升1級
            if i == N1:
                return True
        return False
