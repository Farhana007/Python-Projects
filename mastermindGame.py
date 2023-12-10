

import random


COLORS = ["R","G","B","Y","W","O"]
TRIES = 10
CODE_LENGTH = 4 

#tips:writing uppercase of variabel means these are constant wont change 


def generate_code():
  code = []

  for _ in range(CODE_LENGTH):   #(_) underscore is an place holder like we use x y anything variable
    color = random.choice(COLORS)
    code.append(color)

  return code  


def guess_code():
  guess = input("Guess : ").upper().split("")