# coding:utf-8


class Card():
    '''A playing carc.'''
    RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUIS = ['梅', '方', '红', '黑']  # 梅花，方块，红心，黑桃

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep

    def pic_order(self):
        if self.rank == 'A':
            face_num = 1
        elif self.rank == 'J':
            face_num = 11
        elif self.rank == 'Q':
            face_num = 12
        elif self.rank == 'K':
            face_num = 13
        else:
            face_num = int(self.rank)

        if self.suit == '梅':
            face_suit = 1
        elif self.suit == '方':
            face_suit = 2
        elif self.suit == '红':
            face_suit = 3
        else:
            face_suit = 4

        return (face_suit - 1) * 13 + face_num

    def flip(self):
        self.is_face_up = not self.is_face_up


class PlayerHand():
    '''A hand of playing cards.'''

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '无牌'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Poke(PlayerHand):
    '''A deck of playing cards.'''

    def populate(self):
        for suit in Card.SUIS:
            for rank in Card.RANK:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, player_hands, per_hand=13):
        for rounds in range(per_hand):
            for hand in player_hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                else:
                    print('不能继续发牌了，牌已经发完！')


if __name__ == '__main__':
    print('This is a module with classes for showing playing cards.')
    players = [PlayerHand(), PlayerHand(), PlayerHand(), PlayerHand()]
    poke1 = Poke()
    poke1.populate()
    poke1.shuffle()
    poke1.deal(players, 13)
    n = 1
    for hand in players:
        print('牌手', n, end=':')
        print(hand)
        n = n + 1
    input('\nPress the enter key to exit.')
