# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        """
        1. Convert the linked list to array.
        2. Create a helper function that converts the array to a Binary Search Tree.
        """
        
        # Edge case: if the head is empty
        if not head:
            return None
        
        # Convert 
        nums = []
        
        # point cur to head
        cur = head
        
        # Traverse the linkedlist while it is not empty
        while cur:
            nums.append(cur.val)
            cur = cur.next
            
        # Create helper function to build the BST
        def constructBST(nums, left, right):
            # Edge case if left > right
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            # Build the BST
            node = TreeNode(nums[mid])
            node.left = constructBST(nums, left, mid - 1)
            node.right = constructBST(nums, mid + 1, right)
            return node
        
        return constructBST(nums, 0, len(nums) - 1)
            
        