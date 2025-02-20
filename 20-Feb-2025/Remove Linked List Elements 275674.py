# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur=cur.next
        return dummy.next
    
        