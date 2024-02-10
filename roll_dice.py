import random
roll = random.randint(1,6)
guess = int(input("Guess the number on the dice"))

if guess == roll:
    print("Correct! They rolled a " + str(roll))
else: 
    print ("Wrong! Computer rolled a " +str(roll)) 