# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listSet=set()
        tempA=headA
        while tempA:
            listSet.add(tempA)
            tempA=tempA.next
        tempB = headB
        while tempB:
            if tempB in listSet:
                return tempB
            tempB=tempB.next
        
        return None
            
        
#########

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA,tempB=headA,headB
        while tempA!=tempB:
            tempA=headB if not tempA else tempA.next
            tempB=headA if not tempB else tempB.next
        return tempB