
class calc:
    def __init__(self,operator,num1,num2):
        self.operator=operator
        self.num1=num1
        self.num2=num2

    def oper(self):
        if self.operator==1:
            print ("you selected Addition")
            add=self.num1+self.num2
            print ("The Addition of number 1 and number 2 is ",add)
        elif self.operator==2:
            print ("you selected Subtraction")
            sub=self.num1-self.num2
            print ("The Subtraction of number 1 and number 2 is ",sub)
        elif self.operator==3:
            print ("you selected Multiplication")
            mul=self.num1*self.num2
            print ("The Multiplication of number 1 and number 2 is ",mul)
        elif self.operator==4:
            print ("you selected Division")
            div=self.num1/self.num2
            print ("The Divsion of number 1 and number 2 is ",div)
        else:
            print ("invalid input")


print ("--------Welcome to Python Calculator----------")
print ("----------select the opeartion-----------------")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.Division")
print()
o=int(input("Select Operation:"))
n1=int(input("input first number:"))
n2=int(input("input second nummber:"))
print()
c1=calc(o,n1,n2)
print("--------------------Result--------------------")
c1.oper()
print("--------------------PyJunior--------------------")


