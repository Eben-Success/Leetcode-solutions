# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # Brute Force 
        # Time: O(m * n): list node A and B respectively
        
        # currentA = headA
        # while currentA:
        #     currentB = headB
        #     while currentB:
        #         if currentA == currentB:
        #             return currentA
        #         currentB = currentB.next
        #     currentA = currentA.next
        # return None
        
        # Time: O(n + m)
        # Space: O(1)
        a, b = headA, headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
            
        return a