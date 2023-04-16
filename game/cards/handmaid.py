from card import Card

class Handmaid(Card):
    def __init__(self) -> None:
        super().__init__()

    def image(self) -> str:
        return "handmaid.png"

    def discard(self) -> None:
        self.__owner.giveProtection()
