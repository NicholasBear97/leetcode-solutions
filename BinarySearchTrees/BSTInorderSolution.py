#Name: Nick Bear
#Date: 3/20/2023
#Assignment: Leetcode 94 Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTInorderSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #empty list to store answers
        ans = []

        #define helper function
        #helper function to call recursion with
        def helper(root):

            #check variable so root is not compromised
            check = root

            #if not check, return. Save lines on if statements.
            if not check:
                return
            
            #run helper function on left node
            helper(check.left)

            #add check/root node to answer list
            ans.append(check.val)

            #run helper function on right node
            helper(check.right)

        #call helper function on the global variable (root node)
        helper(root)

        #return the answer that is updated
        return ans
