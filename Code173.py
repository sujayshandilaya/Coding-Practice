# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1,node2=list1,list2 
        
        if not node1:
            return list2
        elif not node2:
            return list1
        
        if node1.val<=node2.val:
            new_head=node1
            node1=node1.next
        else:
            new_head=node2
            node2=node2.next
        new_node=new_head
        while node1 and node2:
            if node1.val<=node2.val:
                new_node.next=node1
                node1=node1.next
            else:
                new_node.next=node2
                node2=node2.next
            new_node=new_node.next
        if not node1:
            new_node.next=node2
        else:
            new_node.next=node1

        return new_head

############################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1,node2=list1,list2 
        new_node=new_head = ListNode(0)
        while node1 and node2:
            if node1.val<=node2.val:
                new_node.next=node1
                node1=node1.next
            else:
                new_node.next=node2
                node2=node2.next
            new_node=new_node.next
        if not node1:
            new_node.next=node2
        else:
            new_node.next=node1
        #new_node.next=node1 or node2
        return new_head.next