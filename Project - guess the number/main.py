import random
randNumber=random.randint(1,100)
# print(randNumber)
userGuess=None
guesses=0

while(userGuess!=randNumber):
    userGuess= int(input("enter your guess: "))
    guesses+=1

    if (userGuess==randNumber):
        print("you guess it right!")
    else:
        if(userGuess>randNumber):
            print("you guess it wrong! enter a smaller number")
        else:
            print("you guess it wrong! enter a larger number")

print(f"you guessed the number in {guesses} guesses")

with open("hiscore.txt","r") as f:
    hiscore=int(f.read())

if (guesses<hiscore):
    print("you have just broken the highest score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))
