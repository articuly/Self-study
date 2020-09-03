# coding:utf-8


class Card:
    """A playing card."""
    RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  # 牌面数字
    SUIT = ['梅', '方', '红', '黑']  # 梅花，方块，红心，黑桃

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank  # 指的是牌面数字1-13
        self.suit = suit  # 指的是花色
        self.is_face_up = face_up  # 是否显示牌面的正面，True为正面

    def __str__(self):  # 打印一张牌的停牌
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep

    def pic_order(self):  # 牌的序号
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

        return (face_suit - 1) * 13 + face_num  # 返回1-52的顺序

    def flip(self):
        self.is_face_up = not self.is_face_up


class PlayerHand:
    """A hand of playing cards."""

    def __init__(self):
        self.cards = []  # cards列表存储牌手的牌

    def __str__(self):  # 打印出牌手的所有牌
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '无牌'
        return rep

    def clear(self):  # 清空手里的牌
        self.cards = []

    def add(self, card):  # 增加牌
        self.cards.append(card)

    def give(self, card, other_hand):  # 把一张牌给到其它牌手
        self.cards.remove(card)
        other_hand.add(card)


class Poke(PlayerHand):
    """A deck of playing cards."""

    def populate(self):  # 生成一副牌
        for suit in Card.SUIT:
            for rank in Card.RANK:
                self.add(Card(rank, suit))

    def shuffle(self):  # 洗牌
        import random
        random.shuffle(self.cards)

    def deal(self, player_hands, per_hand=13):  # 发牌，每人默认13张牌
        for rounds in range(per_hand):
            for player_hand in player_hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    player_hand.add(top_card)
                    # self.give(top_card, player_hand)  # 可以与前两句替换
                else:
                    print('不能继续发牌了，牌已经发完！')


if __name__ == '__main__':
    print('This is a module with classes for showing playing cards.')
    # 初始化4个玩家
    players = [PlayerHand(), PlayerHand(), PlayerHand(), PlayerHand()]
    poke1 = Poke()
    poke1.populate()
    poke1.shuffle()
    poke1.deal(players, 13)
    # 显示4个玩家的牌
    n = 1
    for hand in players:
        print('牌手', n, end=':')
        print(hand)
        n = n + 1
    input('\nPress the enter key to exit.')
