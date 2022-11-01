import random


def who_wins(user, computer):
    if user == computer:
        return "It is a tie"
    elif user == 1 and computer == 2:
        return "The computer wins"
    elif user == 1 and computer == 3:
        return "You win"
    elif user == 2 and computer







def main():
    comp = random.randint(1,3)
    user = int(input("enter a "))

if user == 1:
    choice = "rock"

if user == 2:
    choice = "paper"

if user == 3:
    choice = "scissors"

print("computer is", comp)
print("You are", choice)






'''
if __name__ == '__main__':
    main()
'''