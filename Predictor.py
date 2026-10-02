import random

print("Welcome To Prediction GAME\n")
game = 1
rule = input("Rules pata hai(y/n): ")

if rule == "n":
    print("""Rules are Simple -:
    I have picked a Number from 1 to 100
    You have to guess it
    You have 10 chance""")
    input("Enter To PLAY: ")
else:
    play = input("Game khelna hai(y/n)")
    if play == "n" : game = 0
    else: game = 1

live = 10
num = random.randint(1,101)
guess = int(input("1 se 100 ke beech number do: "))
while live > 0 and game == 1:
    
    if num > guess:
        guess = int(input("isse Bada number do: "))
    elif num < guess:
        guess = int(input("isse Chhota number do: "))
    else:
        print(">>># Haa yahi number tha #<<<")
        again = input("Fir khelna hai(y/n): ")
        if again == "y" or again == "" :
            live = 10
            game = 1
            input("Start New Game: ")
            guess = int(input("1 se 100 ke beech number do: "))
            num = random.randint(1,101)
        else:
            print("Thanks For Playing")
            break
    live -= 1
game = 0
if live == 0: print("## Game Over ##")
