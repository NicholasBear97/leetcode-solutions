#Name: Nick Bear
#Date: 4/14/2023
#Assignment: Leetcode 701 Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTInsertion:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        check = root

        #Empty tree
        #Insert treenode into empty tree
        if (root == None):
            return TreeNode(val)
        
        """ Iteration
        #Search tree and put new treenode in Null spot
        while (check.left or check.right):

            #Finding right most one
            if (check.val < val):

                #If next right is Null, insert here
                if (check.right == None):
                    check.right = TreeNode(val)
                    return root

                #Not null, keep searching
                check = check.right
            
            #finding left most one
            if (check.val > val):
                if (check.left == None):
                    check.left = TreeNode(val)
                    return root

                #Not null, keep searching
                check = check.left
                """
        #Recursion
        #If value is less than check's value, call the function on check.left
        if (check.val > val):
            check.left = self.insertIntoBST(check.left, val)

        #Same but for the right
        if (check.val < val):
            check.right = self.insertIntoBST(check.right, val)   

        return root
