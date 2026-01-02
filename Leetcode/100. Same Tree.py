from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        This approach uses recursion to traverse both trees simultaneously.
        """
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach 2: Iterative Breadth-First Search (BFS)
        This approach uses a queue to compare nodes level by level.
        """
        # Initialize a queue with both roots
        queue = deque([(p, q)])
        
        while queue:
            node_p, node_q = queue.popleft()
            
            # Case 1: Both nodes are None (this level/branch matches)
            if not node_p and not node_q:
                continue
            
            # Case 2: Structural mismatch or value mismatch
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
            
            # Add children to the queue in matching pairs
            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))
            
        