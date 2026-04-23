#week09-3.py 學習計畫Linked List 第3題 (用函士呼叫函示)
#LeetXode 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head  #終止條件

        head2 = head.next
        ans = self.reverseList(head.next)
        head2.next,head.next = head,None
        return ans
