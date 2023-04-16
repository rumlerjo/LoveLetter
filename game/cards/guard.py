from card import Card
from typing import Optional
from game.classes.player import Player

class Guard(Card):
    def __init__(self) -> None:
        super().__init__()

    def rank(self) -> int:
        return 1

    def image(self) -> str:
        return "guard.png"

    def react(self, opponent: Player, guess: Optional[int] = None) -> None:
        cards = opponent.getHand().getCards()
        for card in cards:
            if card.rank() == guess:
                cards.remove(card)
                break

