#creation of stack using list
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append("karthik")
print(stack[2])

# This is a stack implmentation by using list method of a user input
stack = []
def push():
    if len(stack) == n:
        print("The stack is overflow")
    else:
        element = int(input("Enter the element :"))
        stack.append(element)
        print(stack)
      
def pop():
    if len(stack) == 0:
        print("The stack is at underflow")

    else:
        e = stack.pop()
        print("The element which is removed is :",e)
        print(stack)

n = int(input("Enter the limit of the stack"))

while True:
    print("Enter the choice  1. push 2. pop 3.escape")
    
    choice = int(input())
    
    if choice == 1:
        push()
    
    elif choice ==2:
        pop()

    elif choice ==3:
        break
    
    else:
        print("Select the  correct option") 