from card import Card
from game.classes.hand import Hand

class Priest(Card):
    def __init__(self) -> None:
        super().__init__()

    def image(self) -> str:
        return "priest.png"

    def rank(self) -> int:
        return 2
