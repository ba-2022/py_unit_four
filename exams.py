
def gets_a_zero(total_classes, class_missed):
    if class_missed>= 25*total_classes:
        return ("True")
    else:
        return ("False")

def main():

    total_classes = int(input("how many classes are you taking?"))
    class_missed = int(input("How many classes have you missed?"))
    print(gets_a_zero(total_classes, class_missed))

main()



