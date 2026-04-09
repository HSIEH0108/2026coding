#week07-1.py 學習計畫 stack 第2題
#LeetCode 735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans =[]
        for a in asteroids:
            if a > 0 : #正的往右，不會跟左邊的相撞
                ans.append(a)  #直接塞()
            else: #負的往左。可能會跟ans裡的相撞很多次
                while ans and ans[-1]>0:
                    if abs(ans[-1]) == abs(a):#絕對值大小相同都消滅
                        ans.pop() #消滅、吐掉
                        a = 0
                        break #離開迴圈
                    elif abs(ans[-1]) > abs(a): #右邊較小，消滅右邊
                        a = 0
                        break
                    else:#左邊較小消滅左邊
                        ans.pop()
                if a != 0: ans.append(a)
        return ans
