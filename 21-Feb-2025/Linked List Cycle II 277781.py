# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=set()
        cur=head
        while cur:
            if cur in a:
                return cur
            else:
                a.add(cur)
                cur = cur.next
        return 

            
