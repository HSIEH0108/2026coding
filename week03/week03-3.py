#week03-3.py 學習計畫 Sliding Windows
#LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')#把5個字母變成set
        #以後用 if c in vowels:就可以確認它是母音
        count = 0 #紀錄目前有幾個母音
        for i in range(k): #找前面k個字母，逐一檢查，看是不是母音
            if s[i] in vowels: count += 1 #找到1個母音
        ans = count #離開迴圈時，確認前K個字母，有count個母音
        N = len(s) #全部字串長度N
        for i in range(k,N): #右邊每個字母逐一檢查
            if s[i] in vowels: count += 1#右邊的頭s[i]又吃到1母音
            if s[i-k] in vowels:count -= 1
            ans = max(ans,count)#更新答案找最大值
        return ans
