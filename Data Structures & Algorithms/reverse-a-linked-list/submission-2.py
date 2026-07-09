# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            # nextnode
            temp = curr.next
            # reverse curr ptr
            curr.next = prev
            # set new prev
            prev = curr
            # move curr to next node
            curr = temp
        
        return prev