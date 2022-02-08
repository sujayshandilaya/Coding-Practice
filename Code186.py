# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first=last=head
        for i in range(k-1):
            first=first.next
        null_pointer=first
        while null_pointer.next:
            null_pointer=null_pointer.next
            last=last.next
        first.val,last.val=last.val,first.val
        return head

###########################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy=prev_first=prev_last=ListNode(next=head)
        
        first=last=head
        for i in range(k-1):
            prev_first=prev_first.next
            first=first.next
        
        null_pointer=first
        while null_pointer.next:
            null_pointer=null_pointer.next
            prev_last=prev_last.next
            last=last.next
        print(prev_last.val,prev_first.val)
        
        prev_first.next,prev_last.next= last,first
        last.next,first.next=first.next,last.next

        return dummy.next