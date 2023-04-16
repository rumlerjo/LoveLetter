from typing import List
from cards.card import Card


class Deck:
    def __init__(self) -> None:
        self.__cards = List[Card]
