from game.classes.deck import Deck
from typing import Optional, List
from interactions.api import Member
from game.classes.player import Player
from game.classes.cards.card import Card
from random import shuffle

class Game:
    def __init__(self, playerCount: int, players: List[Member]) -> None:
        self.__deck = Deck()
        self.__players = players
        self.__discards: List[Card] = list()
        self.__playerCount = playerCount
        self.__playerReps = [Player(user=self.__players[i]) for i in range(self.__playerCount)]
        shuffle(self.__playerReps)
        self.__turn = 0  

    def startRound(self):
        if (len(self.__discards) > 0):
            for card in self.__discards:
                self.__deck.addCard(card)
        self.__deck.shuffle()
        self.__discards.append(self.__deck.pop())
        for player in self.__playerReps:
            player.resetContention()
            player.removeProtection()
            self.__deck.dealCard(player)
        self.__deck.dealCard(self.__playerReps[self.__turn])
    
    def advanceTurn(self) -> None:
        if self.__turn < self.__playerCount - 1:
            self.__turn += 1
        else:
            self.__turn = 0

    def getDeck(self) -> Deck:
        return self.__deck

    def getPlayers(self) -> List[Member]:
        return self.__players

    def getPlayerClasses(self) -> List[Player]:
        return self.__playerReps

    def getPlayerCount(self) -> int:
        return self.__playerCount
    
    def getTurn(self) -> int:
        return self.__turn
