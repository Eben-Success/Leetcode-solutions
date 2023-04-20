# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Time: O(nlogn)
        # Space: O(log) due to call stacks
        
#         if not head or not head.next:
#             return head
        
#         slow = head
#         fast = head.next
        
#         while fast and fast.next:
#             slow = head.next
#             fast = fast.next.next
            
#         mid = slow.next
#         slow.next = None
        
#         # Recursively divide the linkedlist into two halves
#         left = self.sortList(head)
#         right = self.sortList(mid)
        
#         # Perform Mergesort
#         dummy = ListNode(0)
#         cur = dummy
        
#         while left and right:
#             if left.val < right.val:
#                 cur.next = left
#                 left = left.next
                
#             else:
#                 cur.next = right
#                 right = right.next
#             cur = cur.next
            
#         cur.next = left or right
            
#         return dummy.next

        # Alternative Approach
        # Time: O(nlogn)
        # Space: O(n) due to array
        
        res = []
        cur = head
        
        # if not head or head.next:
        #     return head
        
        while cur:
            res.append(cur.val)
            cur = cur.next
            
        res.sort()
        
        # Create a new list from the sorted array
        dummy = ListNode(0)
        cur = dummy
        
        for val in res:
            cur.next = ListNode(val)
            cur = cur.next
            
        return dummy.next
            
    
    
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        