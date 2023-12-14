
#just genral idea of oop class

x = 1
print(type("Hello"))  #in console we can see what type data type it is 

def hello():
  print("Hello")


print(type(hello))



#Let's create our own class

class Dog: # we are creating dog class
  

  def __init__(self,name):  #init function will be called instanly whenever we create an object we dont need to call it 
    self.name = name  
    print(name)
    

 #here everytime we are passing "self" while creating method in class is becasue
 #  we need to sent the object to the method to specifictly using for the indivitual object   


  def bark(self): #inside dog class we are defining function dog can do like barking 
    print("Bark")


d = Dog("Tim")    #now d is object of dog we are creating from the class Dog and d can perform the function bark
print(d)
#lets print what type d is 

# print(type(d)) # we will be getting this : <class '__main__.Dog'> meaning object of dog

# #now to access the funtion of Dog Class we need to use dot(.)

# d.bark()
