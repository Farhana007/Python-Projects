
# python file extension is .py
print("Hello World")

# python datas are directly saved into computer memory 
#location we can define location with variable where data will be storing


name = "Farhana"
age = 21


name = "Akter"
age = 22

print(name)
print(age)


# user_name = input("What is your Name ? ")
# print(user_name)


#how does python works and how much important dsa is no one can make you understand of this untill and unless
#youre determine enough to make it happen on your own 


old_age = "20"

new_age = str(10) + old_age #type casting

print(new_age)


#writing function


first = 2
second = 4

sum = first + second  
 
print(sum)


#string in python


takeStr = "Titini Stack"

print(takeStr.upper()) #to make all the letter in uppercase
print(takeStr.lower()) #make it lower
print(takeStr.find('S')) #finding any object it will return it's index if not finded will return -1

print(takeStr.find('tini'))

print(takeStr.replace('Titini','Tony'))

print('t' in takeStr)  #cheacking if any word or char prenst in any string , will return true false
print(takeStr)


#arthematic operator (+,-,/,x)

a = 10
print(a)
a += 3
print(a)
a -= 3
print(a)
a *= 3
print(a)
a /= 3
print(a)
a %= 3
print(a)

#// 2 divider to avoid number after decimal(.)

print(5 ** 2) #five to the power 2 double star for power 

#operator precendention mean which operator will be done first / > * > + > -

#comment  is really important so that if any other developer reading your code or even you yourself read it than you can read it n
#and understand your code easily 

#comparison in python  <,>,<= ,>= ,==, !=

print(3 < 2)


#logical Operator in Python OR || AND &&  NOT 

print (3>2 or 3>8)
print (3>2 and 3>8)
print(not 3 > 2)

#if else statement in python

uAge = 14

if uAge >= 18:
	print("Youre an Adult")
	print("You Can Vote")
elif uAge < 18 and uAge > 3:
	print("Youre in School")
else:
    print("youre a child")	



# range in Python means range(5) = 0,1,2,3,4, 

print(range(5)) #here it will return sequence of number but 5 will not be included


#loop in Python

#while loop (jabtak )

i = 1
while i <= 10:
	print(i * "*") #here string will be concataning with number and will be printing number of time
	i += 1


# #For Loop to print object or sequence 

for item in range(5):
	print(item + 1)


	#List In python 

marks = [94,99,94,100]
print(marks)
print(marks[1])
print(marks[-1]) #-1 means starting from otherside 

#making new list from marks
print (marks [0:3])

#adding loop in list 

for score in marks:
	print(score)

#adding anything in list {append}
marks.append(101) #adding in the end
print(marks)

marks.insert(1,87) #to adding in any index 

print(marks)


#to check if something is in list 

print(99 in marks) 

#checking the Length of marks 
print(len(marks))

#itering with while

 
j = 0

while j < len(marks):
	print(marks[j])
	j += 1


#emptying the list 

marks.clear()
print(marks)


#break and Continue

students = ["Ram","Shyam","Karim","Rahim","David"]

for student in students:
	if(student == "Karim"):
		break #now here what break will do is karim is reached this loop will be stopped
	print(student)   


for newStudent in students:
	if(newStudent == "Shyam"):
		continue #here what continue will do is when it reached shayam it will skip shyam and will continue
	print(newStudent)


#mutable meaning changeable , immutable means not changeable 

#tuple : Tuple is like list but it is immuteable


budget = (95,98,97,97,97)

#in tuple we can count any item is avaialbe how many time
print(budget.count(97))
print(budget.index(98))


#set in python  : set doesnot take duplicates just unique values are used in set

lightCount = {99,98,97,38,38,38} # if we print this it will print 38 just one time
print(lightCount) #sets dont have index

for scorrs in lightCount:
	print(scorrs)  #set is unorder list 



#dictonary in python : in dictonary we can store key value pairs

collection = {"math" : 95, "chemistry" : 98,"biology":100}
print(collection)
print(collection["chemistry"])

#to add anything in dictonary

collection["physics"] = 97
print(collection)

#chaning of anything in dictonary

collection["chemistry"] = 99

print(collection)



#Functions in Python 
#  In-Built  - already existed function
#  Module Function  -  like math import math   (from math import sqrt )  print (dir(math))
# User-Defined Functions - which we make ourself


#writing the function by oursel in python 

#def function_name(parameters):  #def means function defination
	#do something


def print_sum(first , second):
	print(first + second)

#function call means using or calling that function

print_sum(1,3)