from game.classes.cards.card import Card
from typing import List, TypeVar

Player = TypeVar("Player")

class Hand:
    def __init__(self, owner: Player) -> None:
        self.__owner = owner
        self.cards: List[Card] = list()

    def addCard(self, card: Card) -> None:
        card.setOwner(self.__owner)
        self.cards.append(card)

    def removeCard(self, card: Card) -> None:
        if card in self.cards:
            self.cards.remove(card)

    def getCards(self) -> List[Card]:
        return self.cards
    
    def maxRank(self) -> int:
        return max([card.rank() for card in self.getCards()])
