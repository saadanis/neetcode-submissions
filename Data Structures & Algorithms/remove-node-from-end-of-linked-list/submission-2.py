# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        zeroth, first, second = None, head, head

        i = 1

        while i <= n:
            second = second.next
            i += 1

        while second:
            second = second.next
            zeroth = first
            first = first.next

        if zeroth:
            zeroth.next = first.next
        else:
            head = first.next

        return head