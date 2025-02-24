# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        previous = None
        while slow:
            nxt = slow.next
            slow.next = previous
            previous = slow
            slow = nxt

        firstHalf = head
        secondHalf = previous
        while secondHalf:
            if firstHalf.val != secondHalf.val:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return True