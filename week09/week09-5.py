#week09-5.py 學習計畫 Linked List 第1題
#LeetCode 2095. Delete the Middle Node of a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:return None
        prev = fast = slow = head #fast兔子 slow 烏龜
        while fast != None and fast.next != None:
            fast = fast.next.next #兔子跳兩格
            prev = slow #烏龜在走時，先記錄前一個位置
            slow = slow.next #烏龜走1格
        #print(slow.val) #當兔子到終點時，烏龜在中間(沒錯)
        prev.next = slow.next
        return head
