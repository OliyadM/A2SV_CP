# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0  

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        count = 0
        cur = self.head
        while cur:
            if count == index:
                return cur.val
            count += 1
            cur = cur.next
        return -1

    def addAtHead(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode
        self.size += 1

    def addAtTail(self, val):
        newnode = Node(val)
        if not self.head:
            self.head = newnode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newnode
        self.size += 1

    def addAtIndex(self, index, val):
        if index > self.size:
            return  
        newnode = Node(val)
        if index == 0:
            newnode.next = self.head
            self.head = newnode
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            newnode.next = cur.next
            cur.next = newnode
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return 
        if index == 0:
            self.head = self.head.next  
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            if cur.next:  
                cur.next = cur.next.next
        self.size -= 1
    