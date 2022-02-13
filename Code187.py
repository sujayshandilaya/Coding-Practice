# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        dummy=prev_slow=ListNode(0)
        dummy.next=prev_slow.next=slow
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            prev_slow=prev_slow.next
        prev_slow.next=slow.next
        return (dummy.next)