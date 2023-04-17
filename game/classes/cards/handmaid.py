from game.classes.cards.card import Card

class Handmaid(Card):
    def __init__(self) -> None:
        super().__init__()

    def image(self) -> str:
        return "handmaid.png"
    
    def rank(self) -> int:
        return 4

    def discard(self) -> Card:
        self.getOwner().giveProtection()
        return super().discard()
