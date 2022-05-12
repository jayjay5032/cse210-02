# Hilo Game
# CSE 210-07: Team B

import random

user_point = 300
random_card_1 = ""
user_input = ""

def main():
    draw_card()
    high_or_low()
    card_compare(random_card_1, user_input)
    ask_continue_game()

def draw_card():
    random_card_1 = random.randrange(1,13)
    print(f"The card is {random_card_1}")

    return random_card_1

def high_or_low():
    user_input = input(print("Higher or lower? (h/l) "))

    return user_input

def card_compare(random_card_1, user_input):
    random_card_2 = draw_card()
    
    if random_card_2 != random_card_1:

        if user_input == "h":
            if random_card_2 > random_card_1:
                user_point += 100

            elif random_card_2 < random_card_1:
                user_point -= 75

        if user_input == "l":
            if random_card_2 > random_card_1:
                user_point -= 75

            elif random_card_2 < random_card_1:
                user_point += 100

    elif random_card_2 == random_card_1:
        draw_card()

    print(f"The next card was: {random_card_2}")

    random_card_1 = random_card_2

    return user_point, random_card_1

def ask_continue_game(user_point):
    if user_point > 0:
        play_again = input(print("Play again? (y/n) "))
    
    return play_again

if __name__ == "__main__":
    main()