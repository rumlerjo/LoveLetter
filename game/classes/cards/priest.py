from game.classes.cards.card import Card
from typing import Optional, List, TypeVar
from game.classes.player import Player

Hand = TypeVar("Hand")

class Priest(Card):
    def __init__(self) -> None:
        super().__init__()

    def image(self) -> str:
        return "priest.png"

    def rank(self) -> int:
        return 2
    
    def react(self, opponent: Player, guess: Optional[int] = None) -> Hand:
        return opponent.getHand()
