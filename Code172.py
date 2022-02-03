# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node=None
        current_node=head
        next_node=None
        while current_node:
            next_node=current_node.next
            current_node.next=prev_node
            prev_node=current_node
            current_node=next_node
        return current_node
###########
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head, None)
    def helper(self, head, node):
        if not head:
            return node
        tmp = head.next
        head.next = node
        return self.helper(tmp, head)