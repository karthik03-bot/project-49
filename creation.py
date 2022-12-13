class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class slinkedlist:
    def __init__(self):
        self.head =None

    def display(self):
        if self.head is None:
            print("The linked list is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end="")
                n = n.ref

    def add_beggining(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
   
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
                n.ref = new_node



l = slinkedlist()
l.add_beggining(10)
l.add_beggining(20)
l.display()
         
        

