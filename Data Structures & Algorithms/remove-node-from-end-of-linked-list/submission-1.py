# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # two pointers. one at 0 and one at n. we keep iterating both until n reaches death.
        # the first pointer points at n we need then.

        zeroth, first, second = None, head, head
        
        if not head or not head.next:
            return

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