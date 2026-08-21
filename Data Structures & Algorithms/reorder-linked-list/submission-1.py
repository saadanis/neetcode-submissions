# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        head2 = slow.next
        slow.next = None

        prev, curr = None, head2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head2 = prev

        curr = head
        curr2 = head2

        while head and head2:
            temp = head.next
            head.next = head2
            head = head.next
            head2 = temp

        


