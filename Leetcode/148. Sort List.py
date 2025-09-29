# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if head is None or there is only one node, it's already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Use slow and fast pointer to find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the list into two halves
        mid = slow.next
        slow.next = None  # Break the link to divide the list
        
        # Step 3: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 4: Merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to merge two sorted linked lists
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach any remaining elements from either list
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        
        return dummy.next  # Return the next node to skip the dummy node