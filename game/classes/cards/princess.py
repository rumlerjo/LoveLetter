from game.classes.cards.card import Card

class Princess(Card):
    def __init__(self) -> None:
        super().__init__()

    def image(self) -> str:
        return "princess.png"
    
    def rank(self) -> int:
        return 8

    def discard(self) -> Card:
        self.__owner.removeFromContention()
        return super().discard()
