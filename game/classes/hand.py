from cards.card import Card
from typing import List

class Hand:
    def __init__(self) -> None:
        self.cards: List[Card] = list()

    def addCard(self, card: Card) -> None:
        self.cards.append(card)

    def removeCard(self, card: Card) -> None:
        if card in self.cards:
            self.cards.remove(card)

    def getCards(self) -> List[Card]:
        return self.cards
