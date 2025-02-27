# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        curr = temp
        while curr.next and curr.next.next:
            f = curr.next
            s = curr.next.next
            f.next = s.next
            s.next = f
            curr.next = s
            curr = f
        return temp.next