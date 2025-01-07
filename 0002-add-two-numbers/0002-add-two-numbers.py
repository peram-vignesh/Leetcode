# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=l1
        cur2=l2
        count=0
        l3=ListNode()
        node=l3
        sum1=0
        while cur1 is not None or cur2 is not None:
            if cur1 is not None and cur2 is not None:
                sum1+=cur1.val
                sum1+=cur2.val
                cur1=cur1.next
                cur2=cur2.next
                node.val=sum1%10
                sum1//=10
            elif cur1 is not None:
                sum1+=cur1.val
                cur1=cur1.next
                node.val=sum1%10
                sum1//=10
            elif cur2 is not None:
                sum1+=cur2.val
                cur2=cur2.next
                node.val=sum1%10
                sum1//=10
            if cur1 is not None or cur2 is not None:
                node.next=ListNode()
                node=node.next
        if sum1!=0:
            print(node.val)
            node.next=ListNode()
            node=node.next
            node.val=sum1
        return l3
                
        