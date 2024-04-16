from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueu(self,item):
        
        new_node = Node(item)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.front.next = new_node
            self.rear = new_node