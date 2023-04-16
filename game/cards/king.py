from card import Card
from game.classes.player import Player
from typing import Optional

class King(Card):
    def __init__(self) -> None:
        super().__init__()

    def rank(self):
        return 6
    
    def image(self) -> str:
        return "king.png"
    
    def react(self, opponent: Player, guess: Optional[int] = None) -> None:
        opponent.__hand, self.__owner.__hand = self.__owner.__hand, opponent.__hand
    