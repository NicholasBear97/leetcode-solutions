#Name: Nick Bear
#Date: 3/13/2023
#Assignment: Leetcode 700 Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTSolution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        #Create a variable to hold the root treenode as a reference
        check = root

        #Check the check variable while it is not null to continue searching for the value given
        while check != None:

            #If the value is found, return check
            if check.val == val:
                return check

            #If the value is not found, set check equal to the appropriate node
            #Nodes on the left side of the tree are smaller than nodes on the right side of the tree, therefore
            #If the value we are searching for is less than the current value, move to the left of the tree
            #If it is higher, move to the right of the tree
            if check.val > val:
                check = check.left
            else:
                check = check.right
        
        #return the node
        return check
