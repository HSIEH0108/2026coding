#week13-1.py 學習計畫 Graph - BFS 第一題
#Leetcode 1926. Nearest Exit from Entrance in Maze
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M , N = len(maze),len(maze[0])
        visited = set()
        visited.add(tuple(entrance))
        queue = deque() #排隊
        queue.append((entrance[0],entrance[1],0))#右邊塞入、排隊

        while queue:
            i,j,step= queue.popleft() #現在處理(i,j)
            for ii , jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii<0 or jj<0 or ii>=M or jj>=N:continue #超過邊界，下一位
                if maze[ii][jj] == '+': continue #遇到牆，下一位

                if(ii,jj) not in visited: #沒到過這一路
                    if ii == 0 or jj==0 or ii == M-1 or jj == N-1:return step+1
                    visited.add((ii,jj)) #標示以處理、排隊中，別重覆排隊
                    queue.append((ii,jj,step+1)) #真的排隊
        return -1
