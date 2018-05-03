
class Stack:                            #Create Stack class
    def __init__(self):
        self.stack=[]                   #Initialize new stack

    def addstack(self,s):               #Method to add objects onto stack
        self.stack.append(s)

    def __str__(self):                  #Method to check the items in a stack
        return str(self.stack)

    def pop(self):  # Method to remove objects on the stack
        return self.stack.pop()


