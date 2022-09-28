# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import random
from typing import Union

import Card


class Collection:
    def __init__(self) -> None:
        """Collection is a base class for holding sets of cards"""
        
        self._cards = []

    def addCard(self, card: Card.Card) -> int:
        """
        Add a card to the collection

        :param card: The card to add
        :type card: Card.Card
        :returns: Index card was added at
        :rtype: int
        """

        self._cards.append(card)
        return len(self._cards) - 1

    def removeCard(self, card: Union[Card.Card,int]) -> Card.Card:
        """
        Remove a given card from the collection. The card may be
        specified by either index or instance

        :param card: Index or instance to remove
        :type card: Card.Card or int
        :returns: The card that was removed
        :rytpe: Card.Card
        """

        if type(card) == "int":
            return self._cards.pop(card)
        else:
            return self._cards.pop(self._cards.index(card))

    def shuffle(self) -> None:
        """
        Pseudo random shuffle the cards
        Uses random.shuffle for pseudo random shuffling
        """
        
        random.shuffle(self._cards)

    def printDeck(self) -> None:
        """Output deck to console"""
        
        for i in self._cards:
            print(f"{i.getParsedValue()} {i.suit}")
