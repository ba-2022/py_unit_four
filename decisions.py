"""def main():
    if 6 > 2:
        print("yes, 6 is bigger than 2")
    print("Thanks for watching")"""

import random


def main():
    number = random.randint(1,10)
    print(number)

    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    print("Thanks for playing")

    main()

