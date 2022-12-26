import math
import sys
import random
from collections import Counter


class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__(self, rank=12, suit='S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__(self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Deck (object):
    # constructor
    def __init__(self, num_decks=1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # deal a card
    def deal(self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)


class Poker (object):
    # constructor
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.players_hands.append(hand)

    # simulate the play of poker
    def play(self):
        # sort the hands of each player and print
        hand_type = []  # create a list to store type of hand
        hand_points = []  # create a list to store points for hand
        hand_vals = []
        checks = [
            self.is_royal, 
            self.is_straight_flush, 
            self.is_four_kind, 
            self.is_full_house, 
            self.is_flush,
            self.is_straight, 
            self.is_three_kind, 
            self.is_two_pair, 
            self.is_one_pair, 
            self.is_high_card
            ]

        for i in range(len(self.players_hands)):
            sorted_hand = sorted(self.players_hands[i], reverse=True)
            self.players_hands[i] = sorted_hand

            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)

            # determine the type of each hand and print
            for check in checks:
                tup = check(sorted_hand)
                if tup[-1]:
                    hand_vals.append((tup[0], tup[1], i + 1))
                    break
            
        print()
        for _, hand_kind, player in hand_vals:
            print(f'Player {player}: {hand_kind}')
        
        print()


        sorted_points = sorted(hand_vals, key=lambda x: x[0], reverse=True)
        max_type = sorted_points[0][1]
        sorted_types = list(filter(lambda x: x[1] == sorted_points[0][1], sorted_points))

        if len(sorted_types) == 1:
            print(f'Player {sorted_types[0][-1]} wins.')
        else:
            for _, _, player in sorted_types:
                print(f'Player {player} ties.')


    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand

    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):
            return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * \
            15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'

    def is_straight_flush(self, hand):
        for i in range(len(hand) - 1):
            if hand[i].suit != hand[i + 1].suit:
                return 0, ''

        start = hand[0].rank

        for i in range(len(hand) - 1):
            if hand[i].rank != start - i:
                return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * \
            15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush'

    def is_four_kind(self, hand):
        four_kind = False
        rank_count = {}
        for i in range(len(hand)):
            rank_count[hand[i].rank] = rank_count.get(hand[i].rank, 0) + 1
            if rank_count[hand[i].rank] == 4:
                four_kind = True
                rank = hand[i].rank
                break

        if not four_kind:
            return 0, ''
        
        same_rank, kicker = [], []
        for i in range(len(hand)):
            if hand[i].rank == rank:
                same_rank.append(hand[i])
            else:
                kicker.append(hand[i])
        
        lst = sorted(same_rank, reverse=True) + kicker

        
        points = 10 * 15 ** 5 + (lst[0].rank) * \
            15 ** 4 + (lst[1].rank) * 15 ** 3
        points = points + (lst[2].rank) * 15 ** 2 + (lst[3].rank) * 15 ** 1
        points = points + (lst[4].rank)

        return points, 'Four Kind'

        
    def is_full_house(self, hand):
        rank_count = {}

        for i in range(len(hand)):
            rank_count[hand[i].rank] = rank_count.get(hand[i].rank, 0) + 1
            if rank_count[hand[i].rank] == 3:
                rank = hand[i].rank
        
        if set(rank_count.values()) != {2, 3}:
            return 0, ''
        
        three_rank, two_rank = [], []
        for i in range(len(hand)):
            if hand[i].rank == rank:
                three_rank.append(hand[i])
            else:
                two_rank.append(hand[i])
        
        lst = sorted(three_rank, reverse=True) + sorted(two_rank, reverse=True)
        
        points = 10 * 15 ** 5 + (lst[0].rank) * \
            15 ** 4 + (lst[1].rank) * 15 ** 3
        points = points + (lst[2].rank) * 15 ** 2 + (lst[3].rank) * 15 ** 1
        points = points + (lst[4].rank)

        return points, 'Full House'
        


    def is_flush(self, hand):
        for i in range(1, len(hand)):
            if hand[i].suit != hand[0].suit:
                return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * \
            15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Flush'


    def is_straight(self, hand):
        for i in range(1, len(hand)):
            if hand[i].rank != hand[i - 1].rank - 1:
                return 0, ''
        
        points = 10 * 15 ** 5 + (hand[0].rank) * \
            15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight'

    def is_three_kind(self, hand):
        three_kind = False
        rank_count = {}

        for i in range(len(hand)):
            rank_count[hand[i].rank] = rank_count.get(hand[i].rank, 0) + 1
            if rank_count[hand[i].rank] == 3:
                rank = hand[i].rank
                three_kind = True
                break
        
        if not three_kind:
            return 0, ''

        three_kind, other = [], []
        for i in range(len(hand)):
            if hand[i].rank == rank:
                three_kind.append(hand[i])
            else:
                other.append(hand[i])
        
        lst = sorted(three_kind, reverse=True) + sorted(other, reverse=True)

        points = 10 * 15 ** 5 + (lst[0].rank) * \
            15 ** 4 + (lst[1].rank) * 15 ** 3
        points = points + (lst[2].rank) * 15 ** 2 + (lst[3].rank) * 15 ** 1
        points = points + (lst[4].rank)
    
        return points, 'Three Kind'


    def is_two_pair(self, hand):
        rank_count = {}

        for i in range(len(hand)):
            rank_count[hand[i].rank] = rank_count.get(hand[i].rank, 0) + 1

        vals_lst = list(rank_count.values())

        if vals_lst.count(2) != 2:
            return 0, ''

        min_rank, max_rank = math.inf, -math.inf
        
        for i in range(len(hand)):
            if rank_count[hand[i].rank] == 2:
                min_rank = min(min_rank, hand[i].rank)
                max_rank = max(max_rank, hand[i].rank) 
            else:
                kicker = hand[i].rank

        lst = [max_rank, max_rank, min_rank, min_rank, kicker]

        points = 10 * 15 ** 5 + (lst[0]) * \
            15 ** 4 + (lst[1]) * 15 ** 3
        points = points + (lst[2]) * 15 ** 2 + (lst[3]) * 15 ** 1
        points = points + (lst[4])
    
        return points, 'Two Pair'


    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair(self, hand):
        one_pair = False
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                rank = hand[i].rank
                one_pair = True
                break
        if (not one_pair):
            return 0, ''

        pair, other = [], []

        for i in range(len(hand)):
            if hand[i].rank == rank:
                pair.append(hand[i])
            else:
                other.append(hand[i])

        lst = sorted(pair, reverse=True) + sorted(other, reverse=True)

        points = 2 * 15 ** 5 + (lst[0].rank) * \
            15 ** 4 + (lst[1].rank) * 15 ** 3
        points = points + (lst[2].rank) * 15 ** 2 + (lst[3].rank) * 15 ** 1
        points = points + (lst[4].rank)

        return points, 'One Pair'

    def is_high_card(self, hand):
        return max(hand[i].rank for i in range(len(hand))), 'High Card'


def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int(line)
    if (num_players < 2) or (num_players > 6):
        return

    # create the Poker object
    game = Poker(num_players)

    # play the game
    game.play()


if __name__ == "__main__":
    main()
