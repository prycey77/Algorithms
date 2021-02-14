
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root == None:
            return -1
        else:
            r_depth = (self.getHeight(root.right))
            l_depth = (self.getHeight(root.left))
            if (l_depth > r_depth):
                return l_depth + 1
            else:
                return r_depth + 1


myTree=Solution()
root=None
nums = [2,5,6,5,7,2,3,4,5,6,3,7]
for i in range(len(nums)):
    data=nums[i]
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       