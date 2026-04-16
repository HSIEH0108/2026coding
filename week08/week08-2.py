# week08-2.py 學習計畫Binary Search 第1題
# 374. Guess Number Higher or Lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #for i in range(1,n+1):
        #   if guess(i) == 0:return i
        #方法1:
        return bisect_left(range(n+1), 0 , key = lambda x:-guess(x))
        #不能用上面的for迴圈，因為n有20億，試不完
        #要用猜數字，每次猜一半
        #方法2:
        left,right = 1,n+1 #左右範圍還沒撞在一起
        while left < right:
            mid = (left + right)//2
            if guess(mid) == 0: return mid
            if guess(mid) > 0 : left = mid + 1 #暗示你再高一點
            else : right = mid #暗示你再低一點
        return left
