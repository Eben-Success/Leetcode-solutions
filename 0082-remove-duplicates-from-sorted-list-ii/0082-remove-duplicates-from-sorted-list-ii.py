# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        
        p, q = dummy, head
        
        while q and q.next:
            if q.val == q.next.val:
                while q and q.next and q.val == q.next.val:
                    q = q.next
                q = q.next
                p.next = q
                
            else:
                p = p.next
                q = q.next
        return dummy.next
        