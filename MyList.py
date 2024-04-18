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
        else:
            return "IndexError"




x = MyList()
x.append(1)
x.append(2.0)
x.append("Hello")
x.append(True)
print(x[4])






    
