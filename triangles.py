def is_triangle(side1, side2, side3):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "These would not make a triangle"
    else:
        return "These would make a triangle"


def main():
    side1 = int(input("side 1 length"))
    side2 = int(input("side 2 length"))
    side3 = int(input("side 3 length"))
    print(is_triangle(side1, side2,side3) )

if __name__ == '__main__':
    main()

