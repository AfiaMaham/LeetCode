# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()  # Initialize the dummy node
        current = dummy  # Pointer to build the result list

        # Single unified loop for l1, l2, and carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)  # Add new node with the digit
            current = current.next

            # Move to the next nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
        