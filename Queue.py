from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self,item):
        
        new_node = Node(item)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.front.next = new_node
            self.rear = new_node

    def dequeue(self):
        
        if self.front == None:
            return "Empty"
        else:
            self.front.next = self.front


    def peek(self):
        if self.front == None:
            return "Empty Queue"

        return self.front.data

    def travers(self):

        if self.front == None:
            return "Empty Queue"
        
        temp = self.front
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next






