# Betelhem Alemu
# 11/10/22
#This program is a black jack game between the user and computer/dealer

import random

'''
This function always either the dealer or user to receive a random card 
and returns a number that ranges from 1-10
'''
def get_card():
    return random.randint(1, 10)

'''
This function adds the users total number of cards:
    :param current: The current value that the user is holding 
    :return: The value of the current cards 
'''
def user_total(current):
    card = get_card()
    print("You drew a", card)
    print("function adds it to", current + card)
    return current + card


'''
This function adds the dealers total number of cards,
The if statement allows the dealer to draw another card if the first card is less
than 15 and it returns the new value of cards that the dealer is holding.
If the number is greater than 15 then it returns the original amount that dealer held

'''
def dealer_total():
    dealer_card1 = get_card()
    dealer_card2 = get_card()
    dealer_card_total = dealer_card1 + dealer_card2
    if dealer_card_total < 15:
        dealer_card3 = get_card()
        return dealer_card3
    else:
        print("Dealer gets no cards")
        return dealer_card_total

'''

This function will tell us who wins:
    :param user: The users total card value
    :param dealer: The dealers total
    :return: what is the outcome
'''
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
In the main it consists of questions that ask the user if they would like another card or not, 
if yes the new card would add to the original value if not it returns the number that the user is holding.
In the end the users and dealers total is show and the get_winner function is called to decide the winner
'''
def main():
    current = 0
    current = user_total(current)
    print("Your current hand is", current)
    users_choice = input("Would you like another card? Type yes or no")
    if users_choice == "yes":
        seconddraw = user_total(current)
        print("Your total is", seconddraw)

        users_choice = input("Would you like another card? Type yes or no")
        if users_choice == "yes":
            thirddraw = user_total(seconddraw)
            print("Your total is", thirddraw)
            users_choice = input("Would you like another card? Type yes or no")
            if users_choice == "yes":
                fourthdraw = user_total(thirddraw)
                print("Your total is", fourthdraw)
            else:
                user_total_final = thirddraw
                print("you are holding at:", thirddraw)
        else:
            user_total_final = seconddraw
            print("you are holding at:", seconddraw)
    else:
        print("you are holding at:",  current)

#prints users and dealers total after everything is added up
    dealer_card_total = dealer_total()
    print("Dealer's total is", dealer_card_total)
    print("User's total is", user_total_final)
    print(get_winner(user_total_final, dealer_card_total))



main()
