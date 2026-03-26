#week05-4.py 2026-03-25珼驹肈
#LeetCode 3546. Equal Sum Grid Partition I
#grid 痻皚
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(row) for row in grid])  #场癬ㄓ

        preSum = 0
        for row in grid: #硋row矪瞶.
            preSum += sum(row) #рrow俱︽癬ㄓ
            if preSum == total - preSum: #场 == 场
                return True
        preSum = 0
        for col in zip(*grid):
            preSum += sum(col)
            if preSum == total - preSum: #オ场 ==场
                return True
        return False
