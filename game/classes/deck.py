from typing import List
from game.classes.cards.card import Card
from game.classes.cards.guard import Guard
from game.classes.cards.priest import Priest
from game.classes.cards.baron import Baron
from game.classes.cards.handmaid import Handmaid
from game.classes.cards.prince import Prince
from game.classes.cards.king import King
from game.classes.cards.countess import Countess
from game.classes.cards.princess import Princess
from game.classes.player import Player
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.__cards: List[Card] = list()
        
        for _ in range(5):
            self.addCard(Guard())
        
        for _ in range(2):
            self.addCard(Priest())
            self.addCard(Baron())
            self.addCard(Handmaid())
            self.addCard(Prince())
        
        self.addCard(King())
        self.addCard(Countess())
        self.addCard(Princess())

        self.shuffle()
    
    def addCard(self, card: Card) -> None:
        self.__cards.append(card)

    def dealCard(self, player: Player) -> Card:
        toDeal = self.__cards.pop()
        player.getHand().addCard(toDeal)
        return Card
    
    def __len__(self) -> int:
        return len(self.__cards)
    
    def shuffle(self):
        shuffle(self.__cards)

    def pop(self) -> Card:
        return self.__cards.pop()