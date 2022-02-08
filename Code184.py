# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        li=[]
        temp=head
        max_sum= float('-inf')
        
        while temp:
            li.append(temp.val)
            temp=temp.next
        
        i,j=0,len(li)-1
        while i<=j:
            max_sum=max(max_sum,(li[i]+li[j]))
            i+=1
            j-=1
        return(max_sum)

##################################################

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def findMiddle(head: Optional[ListNode]):
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            
            return slow
        
        def reverseList(head: Optional[ListNode] ):
            prev_node=None
            next_node=None
            cur_node=head
            while cur_node:
                next_node=cur_node.next
                cur_node.next=prev_node
                prev_node=cur_node
                cur_node=next_node
            return prev_node
            
        middle=findMiddle(head)
        middle.next=reverseList(middle.next)
        temp=middle.next
        temp2=head
        max_sum=float('-inf')
        while temp:
            max_sum=max(max_sum, (temp.val+temp2.val))
            temp=temp.next
            temp2=temp2.next        
        return max_sum