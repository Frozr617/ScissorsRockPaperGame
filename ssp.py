import random
from colorama import Fore, Back, Style
from colorama import init


#Stone = 1
#Sizzors = 2
#Paper = 3

pc = random.randrange(1, 4, 1) #random for the numbers(start, stop, step)

init()
print(Fore.BLACK)
print(Back.MAGENTA)
user = int(input("What do you prefer:\n1.Stone\n2.Scissors\n3.Paper\n"))
print(Back.GREEN)
if pc == 1:
    if user == 1:
        print("It`s a DRAW!")
print(Back.RED)
if pc == 1:
    if user == 2:
        print("Stone brakes scissors! You LOSE!")
print(Back.CYAN)
if pc == 1:
    if user == 3:
        print("Paper wraps stone! You WIN! ")
print(Back.CYAN)
if pc == 2:
    if user == 1:
        print("Stone brakes scissors! You WIN!")
print(Back.GREEN)
if pc == 2:
    if user == 2:
        print("It`s a DRAW")
print(Back.RED)
if pc == 2:
    if user == 3:
        print("Scissors cut paper! You LOSE!")
print(Back.RED)
if pc == 3:
    if user == 1:
        print("Paper wraps stone!You LOSE")
print(Back.CYAN)
if pc == 3:
    if user == 2:
        print("Scissos cut paper! You WIN!")
print(Back.GREEN)
if pc == 3:
    if user == 3:
        print("It`s a DRAW!")

input("Press any button to quit")



