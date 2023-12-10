
#function to play fizzbuzz

def fizzBuzz(n): 
    for num in range(1, n+1):  #for numbe 1 to n
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            
        elif num % 3 == 0:
            print("Fizz")
        
        elif num % 5 == 0:
            print("Buzz")
            
        else:
            print(num) 


print(fizzBuzz(15))           