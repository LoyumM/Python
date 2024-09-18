# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now slow is at the middle of the list
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Now prev is the head of the reversed second half of the list
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:  # second.next to stop after second half is done
            # Store the next pointers temporarily
            tmp1, tmp2 = first.next, second.next
            
            # Reorder nodes
            first.next = second
            second.next = tmp1
            
            # Move to the next nodes
            first = tmp1
            second = tmp2