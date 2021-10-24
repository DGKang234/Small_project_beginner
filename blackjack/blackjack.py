from __future__ import annotations
from typing import Sequence
import random
import collections
import time
import os
import subprocess as sp
import vpython


def clear():
    sp.run(('cls' if os.name == 'nt' else 'clear'), shell=True)

def validate_answer(question: str, choices: Sequence[str]) -> bool:
    while answer == input(question).lower():
        if answer in choices:
            return answer == choices[0]

Y_or_N = 'yn'

Card = collections.nametuple('Card', ['value', 'suit'])

class Deck:

    numbers = [str(v) for v in range(2, 11)] + list('JQKA')
    s_symbol = ['♠','♦','♥','♣']
    suits = "Spades Diamons Hearts Clubs".split()

    def __init__(self, no_deck=1):
        self.no_deck = no_deck
        self.cards = [Card(number, suit) for suit in self.suits for number in self.numbers] * self.no_deck
        self.length = len(self)

    def __repr__(self):
        return "Deck()\n" + ''.join(f"({card.value}--{card.suit})" for card in self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __setitem__(self, position, number):
        sefl.cards[position] = value

    def __draw_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


    # Shuffle when deck is less than 50 % full length
    def is_shuffle_time(self):
        return len(self) < (self.length / 2)

    def shuffle_time(self):
        clear()
        print("Reshuffling the card deck.... \n")
        self.reset()
        self.shuffle()

    def reset(self):
        self.cards = [Card(number, suit) for suit in self.suit for number in self.numbers]

    def deck_visual(self):
        return


class Hand:
    def __init__(self):
        self.hand = []

    def __repr__(self):
        return "Hand()\n" + ''.join(f"{card.number}--{card.suit}") for card in self.hand)

    def add_card(self. *cards: Card) -> None:
        for card in cards:
            self.hand.append(card)

    def remove_card(self):
        return self.hand.pop()

    def hit(self, deck: Deck) -> None:
        card = deck.draw_card
        self.add_card(card)

    def hand_score(self) -> int:
        self.card_no = [10 if card.value in ['J', 'Q', 'K'] else 1 if card.number == 'A' \
                                                else int(card.number) for card in self.hand]

        self.card_scores = dict(zip(self.hand, self.card_no))
        score = 0
        for card in self.hand:
            card_score = self.card_scores[card]
            score += card_score
        if any(card.value == 'A' for card in self.hand) and core <= 11:
            score += 10

        return score

    def card_visual(self):
        return

    def mini_card_visual(self):
        return


class Player(Hand):
    def __init__(self, chips, bet=0, split_cards=False):
        super().__init__()
        self.chips = chips
        self.bet = bet
        self.profit = 0
        self.alive = True
        self.split_cards = split_cards
        self.has_blackjack = False


    def deal_cards(self, deck: Deck) -> None:
        self.hit(deck)
        self.hit(deck)
        print_line('players Cards')
        self.card_visual()
        self.has_blackjack = self.check_for_blackjack()
        self.split_cards = self.check_for_split()
        self.apply_split(deck)

    def add_chis(self, chips: float) -> None:
        self.chips += chips

    def remove_chips(self, chips: float) -> None:
        self.chips -= chips

    def print_balance(self):
        print(f"\nYour blance is currently: £{self.chips:, .2f}\n")

    def check_for_blackjack(self):
        return len(self.hand) == 2 and self.hand_score() == 21

    def check_for_split(self):
        if self.hand[0].value == self.hand[1].value:
            return validate_answer("Do you want to split your cards? : [y / n]: ", Y_or_N)
        return False

    def wager(self):
        while True:
            self.print_balance()
            bet = input(f"How much would you like to bet?: £")
            if not bet.isdecimal():
                continue
            elif float(bet) > self.chips:
                print("sorry, you don't have enough chips. Try again")
            else:
                self.bet = float(bet)
                self.remove_chips(float(bet))
                break

    def add_wager(self):
        while True:
            self.print_balance()
            bet = input(f"Enter additional wager. You may bet up to your original £{self.bet} or less: £")
            if not bet.isdecimal() or float(bet) > self.bet:
                continue
            elif float(bet) > self.chips:
                print("You don't have enough chips. Try again")
            else:
                self.bet_two = float(bet)
                self.remove_chips(float(bet))
                break

    def confirm_double(self):
        return validate_answer("\nYou will only get 1 more card. Confirm you want to double down: [y / n]: ", Y_or_N)    

    def double_down(self, deck: Deck) -> None:
        self.added_wager()
        self.bet += self.bet_two
        #self.visual_move(deck)
        if self.hand_score() > 21:
            self.alive = False

    def apply_split(self, deck: Deck) -> None:
        if self.split_cards:
            self.added_wager()
            self.hand_two = Player(0, split_cards=True, bet=self.bet_two)

            transfer_card = self.remove_card()
            self.hand_two.add_card(transfer_card)
            self.hit(deck)
            self.hand_two.hit(deck)

            print("\nFirst Hand: ")
            #self.mini_card_visual()
            self.player_move(deck)
            print("\nSecond Hand: ")
            self.hand_two.mini_card_visual()
            

    def visual_move()

    def player_move()

    def compute_results()

    def settel()

    def reset()


class Dealer()
    def__init__()

    def deal_cards 

    def reset()

    def card_reveal()

    def dealer_move()

    def dealer_visual



def play_again()

def print_line()

def game()





if __name__ == "__main__"
    __init__()

