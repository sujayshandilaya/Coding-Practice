# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
            if fast==slow: return True
        
        return False
            
###########
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head):
        headset=set()
        node=head
        while node:
            if node in headset:
                return True
            else:
                headset.add(node)
                node=node.next
        return False
        