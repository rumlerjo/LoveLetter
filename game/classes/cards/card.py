from typing import List, TypeVar, Optional

Player = TypeVar("Player")

Card = TypeVar("Card")
Hand = TypeVar("Hand")

class Card:
    """
    A class representing a card and its actions
    """
    ALIASES = {
        1: "Guard",
        2: "Priest",
        3: "Baron",
        4: "Handmaid",
        5: "Prince",
        6: "King",
        7: "Countess",
        8: "Princess"
    }

    def __init__(self) -> None:
        self.__owner = None

    def image(self) -> str:
        return "cardback.png"

    def rank(self):
        return 0

    def __str__(self) -> str:
        return str(self.rank()) + ": " + self.ALIASES.get(self.rank())

    def __repr__(self) -> str:
        return str(self)

    def react(self, opponent: Player, guess: Optional[int] = None) -> Optional[Hand]:
        return None
    
    def discard(self) -> Card:
        """
        Activate discard effects
        """
        self.setOwner(None)
        return self

    def setOwner(self, newOwner: Optional[Player]) -> None:
        self.__owner = newOwner

    def removeOwner(self) -> None:
        self.__owner = None

    def getOwner(self) -> Optional[Player]:
        return self.__owner
