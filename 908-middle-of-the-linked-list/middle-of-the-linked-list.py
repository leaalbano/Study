# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = [head]
        while values[-1].next is not None:
            values.append(values[-1].next)
        return(values[len(values) // 2])

        