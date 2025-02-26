# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
            
        arr=[]
        cur = head

        while cur:
            if cur.val <x:
                arr.append(cur)
            cur = cur.next
        cur  = head

        while cur:
            if cur.val>=x:
                arr.append(cur)
            cur = cur.next

        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]

        arr[-1].next = None

        return arr[0]

    