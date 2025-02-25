# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        slow = temp
        fast = temp.next
        count = 0
        if head == None:
            return head
        while fast.next:
            if slow.next.val == fast.next.val:
                count += 1
                fast = fast.next
                if fast.next == None:
                    slow.next = fast.next
            else:
                if count > 0:
                    slow.next = fast.next
                    fast = slow.next
                else:
                    slow = slow.next
                    fast = fast.next
                count = 0
        return temp.next
        




        