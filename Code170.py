# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        cnt=0
        output=[]
        while node!=None:
            cnt+=1
            node=node.next
        cnt=int(cnt//2)
        if cnt==0:
            return head
        
        node=head
        i=0
        while node!=None:
            i+=1
            node = node.next
            if i==cnt:
                return node

################
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next :
            fast = fast.next.next
            slow=slow.next
        return slow