import ctypes

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0 
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.n

    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B

    def append(self,value):
        if self.size == self.n:
            self.__resize(self.size*2)

        self.A[self.n] = value
        self.n += 1

    def __str__(self):

        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ","


        return '['+result[:-1]+']' 


    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        
        raise IndexError("Item Not Found")


    def pop(self):
        if self.n == 0:
            return "Empty List"
        
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.size = 1
        self.n = 0

        
    def find(self,item):
        
        for i in range(self.n):
            if self.A[i] == item:
                return i
        
        return "Item not found"


    def insert(self,index,item):

        if self.size == self.n:
            self.__resize(self.size*2)

        for i in range(self.n,index,-1):
            self.A[i] = self.A[i-1]

        self.A[index] = item
        self.n += 1



    def __delitem__(self,pos):
        if 0<=  pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]

            self.n -= 1

    def remove(self,item):
        pos = self.find(item)

        if type(pos) == int:
            return self.__delitem__(pos)
        else:
            return pos            



x = MyList()
x.append(1)
x.append(2.0)
x.append("Hello")
x.append(True)
x.append(False)
x.remove("Hello")
print(x)




    
