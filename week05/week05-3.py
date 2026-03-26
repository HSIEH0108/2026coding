#week05-3.py 厩策琜て Hash Table(Map/Set)
#LeetCode 1207. Unique Number of Occurrences
#称ノ
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) #参璸计瞷Ω计
        s = set() #ノㄓ瞷计琌縒礚
        for c in counter: #盢计硋ㄓ
            if counter[c] in s:#狦瞷筁ア毖
                return False
            s.add( counter[c] ) # 瞷硂瞷Ω计s柑
        return True
