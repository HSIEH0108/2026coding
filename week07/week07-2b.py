# week07-2b.py 學習計畫 Stack 第2題
# LeetCode 735. Asteroid Collision
# 正的向右、負的向左，大的會把小的消滅、一樣大、一起死
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a < 0: # 負的往左，可能跟 stack 裡向右的東西相撞
                while stack and stack[-1] > 0: # 目前有存，且頂端向右，會相撞
                    if abs(stack[-1]) == abs(a): # 兩者一樣大，絕對值相等
                        stack.pop() # 左邊消滅了，吐掉
                        a = 0 # 右邊也消滅了
                        break # 離開迴圈
                    elif abs(stack[-1]) > abs(a): # 左邊比較大
                        a = 0 # 右邊被消滅了
                        break
                    else: # 左邊比較小，消滅左邊
                        stack.pop()

            if a != 0: # 如果最後還有剩，就加入 stack
                stack.append(a)

        return stack
