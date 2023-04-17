from game.classes.cards.card import Card

class Countess(Card):
    def __init__(self) -> None:
        super().__init__()

    def image(self) -> str:
        return "countess.png"

    def rank(self) -> int:
        return 7
