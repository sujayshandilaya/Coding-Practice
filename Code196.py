class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1,temp2=l1,l2
        head=op=ListNode()
        head.next=op
        carry=0
        while temp1 or temp2:
            if not temp1:
                temp1=ListNode(0)
            if not temp2:
                temp2=ListNode(0)
            
            num=carry+temp1.val+temp2.val
            carry=num//10
            num=num%10
            op1 = ListNode(num)
            op.next=op1
            op=op.next
            temp1,temp2=temp1.next, temp2.next
        
        if carry!=0:
            op1 = ListNode(carry)
            op.next=op1
        return head.next
            
        