# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def sum(x, y, carry):
            total = x + y + carry
            return total % 10, total // 10

        newnode = ListNode()
        cur = newnode
        carry = 0

        while l1 or l2:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            
            result = sum(val1, val2, carry)
            cur.next = ListNode(result[0])
            carry = result[1]
            cur = cur.next
            
        if carry:
            cur.next = ListNode(carry)

        return newnode.next
