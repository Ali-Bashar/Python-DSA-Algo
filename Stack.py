from Node import Node

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self,value):
        
        new_node = Node(value)

        self.top = new_node
