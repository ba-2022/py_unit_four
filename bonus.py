# Betelhem Alemu
# 10/26/22
def salary_calculator(longevity, current):
    if longevity > 5:
        salary = current + (current * 0.05)
    else:
        salary = current
    return salary


def main():
    longevity = int(input("How many years have you worked here:"))
    current = int(input("What is your current salary:"))
    final = salary_calculator(longevity, current)
    print("salary is:", int(round(final)))



main()
