# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=temp1=head
        
        while temp1:
            while temp1 and temp1.val == temp.val:
                temp1=temp1.next
            temp.next=temp1
            temp=temp1
        return head
###############

class Solution:
    def deleteDuplicates(self, head):
	    if not head or not head.next:
		    return head
	    h = self.deleteDuplicates(head.next)
	    head.next = h if head.val != h.val else h.next
	    return head