# Betelhem Alemu
# 10/27/22
# Absolute Value Calculator


def absolute(number):
    absNum = abs(number)
    return absNum

def main():
    number = int(input("Please enter a number"))
    print("The absolute value of ", number, "is", absolute(number))


if __name__ == '__main__':
    main()