# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li=[] 
        while head:
            li.append(head.val)
            head=head.next
        i=0
        j=len(li)-1
        while i<=j:
            if li[i]!=li[j]:
                return False
            i+=1
            j-=1
        return True
            
###################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle=head
        fast=head.next
        cnt=0
        while fast and fast.next:
            fast=fast.next.next
            middle=middle.next
        print(middle.val)
        cur_node=middle.next
        prev_node=None
        next_node=None
        while cur_node:
            next_node=cur_node.next
            cur_node.next=prev_node
            prev_node=cur_node
            cur_node=next_node
        while prev_node:
            if prev_node.val != head.val:
                return False
            prev_node=prev_node.next 
            head=head.next
        return True
        
