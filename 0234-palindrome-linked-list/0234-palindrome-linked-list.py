# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        cur = head
        
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
            
        return True if res == res[::-1] else False
    
#         # Using O(n) Time and O(1) Space
        
#         slow = head
#         fast = head.next
        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#         # Reverse the second half of the linkedlist
#         prev, cur = None, slow
        
#         while cur:
#             nxt = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nxt
            
#         # Compare the two halves of the linkedlist
#         first_half, second_half = head, prev
        
#         while second_half:
#             if second_half.val != first_half.val:
#                 return False
            
#             second_half = second_half.next
#             first_half = first_half.next
            
#         return True
        
        
        
        
        
        
        
        