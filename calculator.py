
# Creating an Calculator in Python 
#without writing function 


first = input( "Enter First Number : ")

operator = input ("Enter operator ( + , - , * , / , % ) : ")

second = input ("Enter Second Number : ")


#type casting input int in 
first = int(first)
second = int(second)

if operator == "+":
  print(first + second)
elif operator == "-":
  print(first - second)
elif operator == "*":
  print(first * second)   
elif operator == "/":
  print(first // second)
elif operator == "%":
  print(first % second)  
else:
  print("Invalid Operation")
