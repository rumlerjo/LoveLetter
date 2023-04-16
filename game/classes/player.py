from hand import Hand
from cards.card import Card
from typing import Optional, TypeVar
from interactions.api import Member

Player = TypeVar("Player")

class Player:
    def __init__(self, user: Optional[Member] = None) -> None:
        self.__hand = Hand()
        self.__points = 0
        self.__protected = False # whether protected by handmaid
        self.__user = user
        self.__inContention = True # whether player is still in the round

    def getUser(self) -> Member:
        return self.__user

    def getHand(self) -> Hand:
        return self.__hand

    def winRound(self) -> None:
        self.__points += 1

    def giveProtection(self) -> None:
        self.__protected = True

    def removeProtection(self) -> None:
        self.__protected = False

    def removeFromContention(self) -> None:
        self.__inContention = False

    def resetContention(self) -> None:
        self.__inContention = True

    def isIncontention(self) -> bool:
        return self.__inContention

    def canBeAttacked(self) -> bool:
        """
        Return whether this player can be attacked
        :return: bool representing the protected status of player
        """
        return self.__protected
