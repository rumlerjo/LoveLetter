from game.classes.cards.card import Card
from typing import Optional, TypeVar
from game.classes.player import Player

Hand = TypeVar("Hand")

class Baron(Card):
    def __init__(self) -> None:
        super().__init__()

    def rank(self) -> int:
        return 3
    
    def image(self) -> str:
        return "baron.png"
    
    def react(self, opponent: Player, guess: Optional[int] = None) -> Optional[Hand]:
        oppHighest = opponent.getHand().maxRank()
        myHighest = self.getOwner().getHand().maxRank()
        self.getOwner().removeFromContention() if oppHighest > myHighest else opponent.removeFromContention()
