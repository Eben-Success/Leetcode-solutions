# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node and point it to the head
        dummy = ListNode(-1)
        dummy.next = head
        
        # set two pointers 
        prev = dummy
        cur= head
        
        # Traverse the linkedlist and swap every two nodes
        while cur and cur.next:
            # point the previous node to the current node
            prev.next = cur.next
            
            # point the first node to the third node
            cur.next = cur.next.next
            
            # point the second node to the first (swapping)
            prev.next.next = cur
            
            # update the pointers for the next iteration
            prev = cur
            cur = cur.next
            
        return dummy.next