from Node import Node

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self,value):
        
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def size(self):

        if self.top == None:
            return "Empty Stack"
        
        temp = self.top
        count = 0

        while temp != None:
            temp = temp.next
            count += 1
        return count


