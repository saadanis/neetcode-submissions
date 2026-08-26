# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        resultHead = ListNode()
        resultCurrent = resultHead

        heap = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        while heap:
            _, i, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            resultCurrent.next = node
            resultCurrent = resultCurrent.next
        
        return resultHead.next
