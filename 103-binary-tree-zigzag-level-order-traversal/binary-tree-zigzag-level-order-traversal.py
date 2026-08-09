# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = collections.deque([root])
        ans = []
        left_to_right = True
        
        while q:
            # Using a deque for the level lets us efficiently append to either end
            level = collections.deque() 
            
            for _ in range(len(q)):
                node = q.popleft()
                
                # This is where the zigzag happens!
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                # The queue ALWAYS processes children left-to-right
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            ans.append(list(level))
            left_to_right = not left_to_right
            
        return ans