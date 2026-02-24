
values=list(map(int,input("enter values in a BST pattern:").split()))
class node:
     def __init__(self,data):
         self.data=data
         self.left=None
         self.right=None
def insert(root,value):
    if root is None:
        return node(value)
    if value<root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
def inorder(root):
    if root:
        pre_order(root.left)
        print(root.data,end=" ")
        pre_order(root.right)
root=None
for v in values:
    root = insert(root,v)
print("Pre_order Traversal",inorder(root))            

