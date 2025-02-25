# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a=[]
        cur = head

        while cur:
            a.append(cur.val)
            cur = cur.next
        
        n=len(a)//2
        m=0
        a=a[::-1]
        cur = head

        for i in range(n):
            s = a[i]+cur.val
            m=max(m,s)
            cur = cur.next

        return m

        l
            