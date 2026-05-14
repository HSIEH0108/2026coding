#week12-1a.py 學習計畫 Graph - DFS第一題
#LeetCode 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0] #我們利用stack裡面有待處理的房間，一開始房間是0 開的
        visited = set()
        visited.add(0) #已經排好、代處理，下次有拿到鑰匙，不要再放入Stack
        while stack:
            now = stack.pop() #吐出1個房間
            for k in rooms[now]: #把房間哩，所有的鑰匙k，都拿來檢查
                if k in visited:continue
                #如果走到這裡，代表沒走過，沒有待處理房間k
                stack.append(k)
                visited.add(k) #標記這個房間也待處理、不要再處理
        return len(rooms) == len(visited) #房間裡的樹木，全部都參觀過了，成功
