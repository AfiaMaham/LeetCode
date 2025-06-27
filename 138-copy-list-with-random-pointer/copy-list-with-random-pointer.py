"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        
        while curr:
            nxt = curr.next
            newNode = Node(curr.val)
            curr.next = newNode
            newNode.next = nxt
            curr = curr.next.next

        curr = head
        while curr:
            copy = curr.next
            rand = curr.random
            if rand == None:
                copy.random = None
            else:
                copy.random = rand.next
            curr = curr.next.next

        curr = head.next
        dummy = None
        while curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return head.next

        
        