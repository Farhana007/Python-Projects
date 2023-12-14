
# Creating an Calculator in Python 
#without writing function 


first = input( "Enter First Number : ")

operator = input ("Enter operator ( + , - , * , / , % ) : ")

second = input ("Enter Second Number : ")


#type casting input int in 
first = int(first)
second = int(second)

# if operator == "+":
#   print(first + second)
# elif operator == "-":
#   print(first - second)
# elif operator == "*":
#   print(first * second)   
# elif operator == "/":
#   print(first // second)
# elif operator == "%":
#   print(first % second)  
# else:
#   print("Invalid Operation")



#calculator using  class

class Calculator():
  def plus(self,a,b):
    print(a+b)
  

  def minus(self,a,b):
    print(a-b)
   

  def increse(self,a,b):
    print(a*b)
   

  def divide(self,a,b):
    print(a/b)


  def module(self,a,b):
    print(a%b)
  

  def error():
    print("Invalid")

  
calculator = Calculator() 

if operator == "+":
  calculator.plus(first,second)
elif operator == "-":
  calculator.minus(first,second)
elif operator == "*":
  calculator.increse(first,second)   
elif operator == "/":
  calculator.divide(first,second)
elif operator == "%":
 calculator.module(first,second)
else:
  calculator.error()
