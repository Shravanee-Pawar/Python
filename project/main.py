'''
1 for snake
-1 for water
0 for gun

'''
import random

computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (s = Snake, w = Water, g = Gun): ")

youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

you = youDict[youstr]

print("You chose:", reverseDict[you])
print("Computer chose:", reverseDict[computer])

if computer == you:
    print("It's a draw!")
elif (computer == -1 and you == 1) or \
     (computer == 1 and you == 0) or \
     (computer == 0 and you == -1):
    print("You win!")
else:
    print("You lose!")