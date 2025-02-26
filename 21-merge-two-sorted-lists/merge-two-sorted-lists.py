# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-100)
        temp.next = list1
        currList1 = temp
        currList2 = list2
        while currList2 and currList1 and currList1.next:
            if currList2.val >= currList1.val and currList2.val <= currList1.next.val:
                nxt = currList1.next
                currList1.next = currList2
                nxt2 = currList2.next
                currList2.next = nxt
                currList2 = nxt2
            currList1 = currList1.next
        if currList2:
            currList1.next = currList2
        return temp.next
            


