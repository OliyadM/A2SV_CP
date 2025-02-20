# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=set()
        cur = head 
        while cur:
            if cur in a:
                return pos
            else:
                a.add(cur)
                cur=cur.next
        return False

