# Create a class return sum of square of 3 given number class name should be Point
class Point:
    def __init__(self,num1=0,num2=0,num3=0):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        
    def qursum(self):
        self.sm=self.num1**2+self.num2**2+self.num3**2
        return self.sm
    
n1=int(input("Enter the 1st number\n"))
n2=int(input("Enter the second number\n"))
n3=int(input("Enter the 3rd number\n"))

result=Point(n1,n2,n3)
print(f"{result.qursum()} is sum of 3 number")
        