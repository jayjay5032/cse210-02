# Hilo Game
# CSE 210-07: Team B

from card import Card

class Director:
    def __init__(self):
        self.card1 = Card()
        self.is_playing = True
        self.user_point = 300
        self.user_input = ""

    def start_game(self):
        while self.is_playing:
            self.draw_card()
            self.high_or_low()
            self.card_compare()
            self.game_response()
            self.ask_continue_game()

    def draw_card(self):
        self.card1.roll()
        return self.card1.value

    def high_or_low(self):
        print(f"The card is {self.card1.get_value()}")
        self.user_input = input("Higher or lower? (h/l) ")
        return self.user_input

    def card_compare(self):
        random_card_1 = self.card1.value
        random_card_2 = self.draw_card()
        
        
        if random_card_2 != random_card_1:

            if self.user_input == "h":
                if random_card_2 > random_card_1:
                    self.user_point += 100
                    self.state = True

                elif random_card_2 < random_card_1:
                    self.user_point -= 75
                    self.state = False

            elif self.user_input == "l":
                if random_card_2 > random_card_1:
                    self.user_point -= 75
                    self.state = False

                elif random_card_2 < random_card_1:
                    self.user_point += 100
                    self.state = True

        elif random_card_2 == random_card_1:
            self.draw_card()

        print(f"The next card was: {random_card_2}")

        random_card_1 = random_card_2

        return self.user_point, self.state

    def game_response(self):
        
        if self.state == True:

            print("Congratulations on winning! You have gone up by 100 points!")

        elif self.state == False:

            print("It seems you have lost. Your points have been reduced by 75 points!")

    def ask_continue_game(self):
        print(f"Your point is: {self.user_point}")
        if self.user_point > 0:
           self.user_input = input("Play again? (y/n) ")
           if self.user_input == "n":
                print("Thank for palying!")
                self.is_playing = False
        else:
            self.is_playing = False
            print("Thank for playing!")
        return self.is_playing

director = Director()
director.start_game()