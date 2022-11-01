def is_divisible(num1, check):
    if int(num1) % int(check) == 0:
        return True
    else:
        return False



def main():

    # Get the two pieces of input from the user.
    num1 = int(input("What is the first number? "))
    check = int(input("What is the second number? "))

    if is_divisible(num1, check):
        print(num1, "is divisible by", check)
    else:
        print(num1, "is not divisible by", check)


if __name__ == '__main__':

    main()
