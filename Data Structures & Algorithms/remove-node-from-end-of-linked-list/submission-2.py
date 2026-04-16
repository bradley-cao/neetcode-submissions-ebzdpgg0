# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head 
        size = 1

        while ptr.next != None:
            ptr = ptr.next
            size += 1
        
        size -= n

        if size == 0:
            return head.next
            
        ptr = head

        while size > 1 and ptr.next != None:
            ptr = ptr.next
            size -= 1

        if ptr.next == None:
            return None
        
        ptr.next = ptr.next.next

        return head
