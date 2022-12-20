# Day 11 Project
# Blackjack Capstone Project

import random
import pyautogui

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

dealer = []
player = []

def new_game():
    """
    Clear the screen, start a new game, print the logo, and
    Deal two cards each to dealer (computer) and player.
    """
    pyautogui.hotkey('ctrl', 'tab', 'c')
    dealer.clear()
    player.clear()
    print(logo)
    for _ in range(2):
        dealer.append(deal_card())
        player.append(deal_card())

def deal_card():
    """return one random card from the infinite deck of cards."""
    deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck_of_cards)

def check_blackjack(cards):
    """check if the given cards represent blackjack or not."""
    if sum(cards) == 21:
        return True
    else:
        return False

def current_score():
    """
    Display current score:
    Player's cards and total score +
    Computer's first card.
    """
    print(f"\tYour cards: {player}, current score: {sum(player)}")
    print(f"\tComputer's first card: {dealer[0]}")

def final_score():
    """
    Display final score:
    Player's and dealer's final hand and their respective sums.
    """
    print(f"Your final hand: {player}, final score: {sum(player)}")
    print(f"Computer's final hand: {dealer}, final score: {sum(dealer)}")

def went_over(cards):
    """
    Check if the sum of given cards has gone over 21.
    (Adjust the value of ace card if needed.)
    """
    if sum(cards) > 21:
        if 11 in cards:
            cards[cards.index(11)] = 1
            return False
        else:
            return True
    else:
        return False

def calculate_score():
    """Calculate and print final score."""
    if sum(dealer) > sum(player):
        print("You lose 😤")
    elif sum(dealer) == sum(player):
        print("Draw 🙃")
    elif sum(dealer) < sum(player):
        print("You win 😃")


while True:
    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if play_game == 'y':
        new_game()
        game_over = False

        if check_blackjack(dealer):
            final_score()
            print("Computer has blackjack. You lose.")
            continue
        elif check_blackjack(player):
            final_score()
            print("You have blackjack. You win.")
            continue

        while True:
            current_score()
            pick_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if pick_card == 'y':
                player.append(deal_card())
                if went_over(player):
                    final_score()
                    print("You went over. You lose 😤")
                    game_over = True
                    break
            else:
                break
        if game_over:
            continue

        while sum(dealer) < 17:
            dealer.append(deal_card())
            if went_over(dealer):
                print("Opponent went over. You win 😁")

        calculate_score()
    else:
        break
