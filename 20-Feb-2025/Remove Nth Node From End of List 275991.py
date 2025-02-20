# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        size=0

        while cur:
            cur=cur.next
            size+=1
        index = size-n

        if index == 0:
            if head:
                head = head.next
                return head


        count=0

        cur= head
        while cur.next:
            if count == index-1:
                cur.next = cur.next.next
                return head
            else:
                count+=1
                cur=cur.next
        return head
