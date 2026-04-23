#week09-2.py 學習計畫Linked List 第3題
#LeetXode 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head: #只要還有資料
            a.append(head.val)
            head = head.next #換下一筆
        now = ans = ListNode() #答案將串到裡面
        #下面用倒過來的迴圈，把陣列值，逐一串到ans後面
        N = len(a) #陣列的長度
        for i in range(N-1,-1,-1):
            now.next = ListNode(a[i])
            now = now.next
        return ans.next
