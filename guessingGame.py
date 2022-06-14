from importlib import import_module


import random

print("Number Guessing Game")
print("Guess a number between 1-9")
print("enter your guess:")
x=input()
#question1
print(" guess a number greater than" + x)
y=input()
if x<y:
    print("you are right!!")
else: 
    print("better luck next time")

#question2
print(" guess a number lesser than" + y)
z=input()
if y>z:
    print("you are right!!")
else: 
    print("better luck next time")

#question3
print(" guess a number lesser than" + z)
a=input()
if z>a:
    print("you are right!!")
else: 
    print("better luck next time")

#question 4
print(" guess a number greater than" + a)
b=input()
if a<b:
    print("you are right!!")
else: 
    print("better luck next time")

#question 5
o=(random.randrange(1,9))
print("enter a number greater than" + o )
c=input()
if c>o:
    print("You won!!!")
else:
    print("you lost")