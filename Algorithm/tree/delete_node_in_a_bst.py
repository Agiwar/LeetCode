from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find_min_node(root: Optional[TreeNode]) -> Optional[TreeNode]:
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_val_node = find_min_node(root.right)
                root.val = min_val_node.val
                root.right = self.deleteNode(root.right, min_val_node.val)
        
        return root
