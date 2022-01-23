class A:
    def __init__(self,num2):
        self.__num1=10
        self.num2=num2
    def display(self):
        print(self.__num1)
class B(A):
    def __init__(self,num2):
        self.num2=num2
        self.__num1=30
    
b=A(40)
b.display()
#print(b.__num1)