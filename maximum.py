
def max(num1, num2):

     if num1 > num2 :
        print(str(num1) + " is larger" + (num2))

     if num1 < num2:

        print(str(num1) + " is smaller" + (num2))

def main():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    max(num1,num2)


main()