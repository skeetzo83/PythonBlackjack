import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
total_user = []
total_computer = []
#deal card function
def deal_card(x):
    return random.choice(cards)
#variables to use
user_cards = [deal_card(cards), deal_card(cards)]
computer_cards = [deal_card(cards), deal_card(cards)]
total_user = []
total_computer = []
#calculate score function
def calculate_score():
    total_user = sum(user_cards)
    total_computer= sum(computer_cards)
    for position in range(len(user_cards)):
        if total_user > 21 and user_cards[position] == 11:
            total_user -= 10
    for position1 in range(len(computer_cards)):
        if total_computer > 21 and computer_cards[position1] == 11:
            total_computer -= 10
    else:
        return [total_user, total_computer]
#end of calculate score function
    
    
    
#start of the program
print(f"Your cards: {user_cards}, current score: {calculate_score()[0]}") 
print(f"Computer's first card: {computer_cards[0]}")
#- create a while function to repeat draw cards
not_end = False
while not not_end: 
    draw = input("Type 'y' if draw another card, type 'n' if hold")
    if draw == "y":
        user_cards.append(deal_card(cards))
        calculate_score()
        print(f"  your cards {user_cards}, current score {calculate_score()[0]}\n  Computer's first card {computer_cards[0]}")
        if calculate_score()[0] >= 21:
            not_end = True
    if draw == "n":
        not_end = True
    
#end of while loop
computer_end = False
while not computer_end:
    if calculate_score()[1] < 17:
        computer_cards.append(deal_card(cards))
    else:
        computer_end = True
print(f"  Your final hand: {user_cards}, final score: {calculate_score()[0]}\n  Computer's final hand: {computer_cards}, final score: {calculate_score()[1]}")
if calculate_score()[0] > 21:
    print("You went over. You Lose")
elif calculate_score()[0] == 21:
    print("  You win Blackjack")
elif calculate_score()[0] > calculate_score()[1]:
    print("You win")
elif calculate_score()[0] < calculate_score()[1]:
    print("You Lose")
elif calculate_score()[0] == calculate_score()[1]:
    print("It's a draw")
print(calculate_score()[0], calculate_score()[1])




