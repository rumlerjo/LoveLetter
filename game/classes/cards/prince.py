from game.classes.cards.card import Card
from typing import Optional
from game.classes.player import Player

class Prince(Card):
    def __init__(self) -> None:
        super().__init__()

    def rank(self) -> int:
        return 5

    def image(self) -> str:
        return "prince.png"

    def react(self, opponent: Player, guess: Optional[int] = None) -> None:
        oppCards = opponent.getHand().getCards()
        for card in oppCards:
            # sibling rivalry
            if self.ALIASES.get(card.rank()) == "Princess":
                opponent.getHand().removeCard(card)
                break
        
