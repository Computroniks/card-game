# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import random
from typing import Union

import Card

class CollectionIter:
    def __init__(self, collection) -> None:
        """
        Itterator for the Collection class
        """
        
        self._cards = collection.cards
        self._index = 0

    def __iter__(self):
        """
        Iter method for Collection

        :rtype: CollectionIter
        """
        
        return self

    def __next__(self) -> str:
        """
        Get the next item

        :rtype: str
        :raises: StopIteration
        """
        
        if self._index < len(self._cards):
            self._index += 1
            return str(self._cards[self._index-1])
        else:
            raise StopIteration
    

class Collection:
    def __init__(self) -> None:
        """
        Collection is a base class for holding sets of cards

        The cards are represented as an array with the end of said
        array representing the top of the deck.
        """
        
        self._cards = []

    def __iter__(self):
        """
        Custom iterator
        """
        return CollectionIter(self)

    @property
    def cards(self) -> list[Card.Card]:
        """List of all cards in collection. 0 is bottom card"""
        
        return self._cards

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

    def addCardByIndex(self, card: Card.Card, index: int) -> None:
        """
        Add a card to the collection at the specified index

        :param card: The card to add
        :type card: Card.Card
        :param index: Index to add card at
        :type index: int
        """

        self._cards.insert(index, card)

    def addCardBottom(self, card: Card.Card) -> None:
        """
        Add a card to the bottom of the collection

        :param card: The card to add
        :type card: Card.Card
        """

        self.addCardByIndex(card, 0)

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

        for i in range(len(self._cards*2)):
            i1 = random.randint(0, len(self._cards)-1)
            i2 = random.randint(0, len(self._cards)-1)
            self._cards[i1], self._cards[i2] = self._cards[i2], self._cards[i1]

    def printDeck(self) -> None:
        """Output deck to console"""
        
        for i in self._cards:
            print(i)


class Deck(Collection):
    def __init__(self, ace_high = False) -> None:
        """
        Create an instance of Deck

        :param ace_high: Should a high or low ace be used?, defaults to False
        :type ace_high: bool, optional
        """
        
        super().__init__()
        self._generateDeck(ace_high)
        self.shuffle()

    def _generateDeck(self, ace_high: bool ) -> None:
        """
        Generate a deck

        :param ace_high: Should Ace be 1 or 14. Set to True if 14
        :type ace_high: bool
        """
        
        suits = ["hearts", "dimonds", "clubs", "spades"]
        if ace_high:
           card_range = (2,15)
        else:
            card_range = (1,14)
            
        for suit in suits:
            for i in range(card_range[0], card_range[1]):
                self.addCard(Card.Card(suit, i))


class Pile(Collection):    
    pass
