# Betelhem Alemu
# 11/1/22
import random
def get_card():
    return random.randint(1, 11)

def user_total(current):
    card = get_card()
    print("You drew a", card)
    return current + card

def dealer_total():
    dealer_card1 = get_card()
    dealer_card2 = get_card()
    dealer_card_total = dealer_card1 + dealer_card2
    print("dealer total is", dealer_card_total)

def get_winner(user, dealer):
    if user > 21 and dealer > 21:
        return "Both lose"

    elif user == dealer:
        return "It's a tie"

    elif user > 21:
        return "user loses"

    elif dealer > 21:
        return "dealer loses"

    elif user > dealer:
        return "user wins"

    elif dealer > user:
        return "dealer wins"


'''

This function will tell us who wins:
    :param user: The users total card value
    :param dealer: The dealers total
    :return: what is the outcome
'''

def main():
    current = 0
    current = user_total(current)
    print("Your total is", current)
    users_choice = input("Would you like another card? Type yes or no")
    if users_choice == "yes":
        card = current
        print("Your total is", user_total(current) + card)
    else:
        print("your total is",  current)

main()
