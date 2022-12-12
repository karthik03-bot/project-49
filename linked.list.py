class Node:
    def __init__(self,data):
        self.data = None
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None


def print_LL(self):
    if self.head is None:
        print("the linked lsit is empty ")
    
    else:
        n = self.head
    
    while n is not None:
        print(n.data)
        n= n.next


LL1 = linkedlist()
LL1.head = Node(1)