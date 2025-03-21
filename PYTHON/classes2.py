class Calculator:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def sum(self):
        print("Sum:",self.a+self.b)
    def subtract(self):
        print("Difference:",self.a-self.b)
    def product(self):
        print("Product:",self.a*self.b)
    def division(self):
        print("Division:",self.a/self.b)
    
u=int(input("Enter the a value"))
v=int(input("Enter the b value"))
Cal=Calculator(u,v)
choice=int(input("Enter the operation you would like to perform:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide"))
if(choice==1):
    print(Cal.sum())
elif(choice==2):
    print(Cal.subtract())
elif(choice==3):
    print(Cal.product())
elif(choice==4):
    print(Cal.division())
else:
    print("Thankyou...")
end;