class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cnt=0
        temp=list1
        while temp.next:
            if cnt==(a-1):
                temp1=temp.next
                while temp1:
                    if cnt==(b):
                        break
                    cnt+=1
                    temp1=temp1.next
                temp.next=list2
            cnt+=1
            temp=temp.next

####################################
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cnt=0
        temp=list1
        for i in range(b+1):
            if i==(a-1):
                temp_a=temp
            temp=temp.next
        temp_b=list2
        while temp_b.next:
            temp_b=temp_b.next
        temp_a.next=list2
        temp_b.next=temp
        return list1