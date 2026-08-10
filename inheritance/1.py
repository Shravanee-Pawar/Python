class twoDVector:
    def __init__(self , i , j):
        self.i = i
        self.j = j
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")    
class threeDvector(twoDVector):
    def __init__(self , i ,j,k):
        super().__init__(i,j)
        self.k =k  
        
    def show(self):
            print(f"the vector is {self.i}i + {self.j}j") 
a = twoDVector(1,2)
a.show()

b = threeDvector(5,2,3)
b.show()            