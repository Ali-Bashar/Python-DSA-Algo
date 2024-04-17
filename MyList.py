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



x = MyList()
print(len(x))