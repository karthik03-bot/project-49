class Node:
    def __init__(self,data): #creation of a tree and printing it 
        self.left = None
        self.right = None
        self.data = data
root = Node(1)
root.left = Node(2)
root.right = Node(3)
print("The root Node is :",root.data)
print("The root Node left is :",root.left.data)
print("The root Node right is :",root.right.data)
