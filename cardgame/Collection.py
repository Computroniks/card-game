# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import random

from Card import Card


class Collection:
    def __init__(self) -> None:
        self._cards = []

    def addCard(self, card: Card.Card) -> int:
        self._cards.append(card)
        return len(self._cards) - 1

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def printDeck(self) -> None:
        for i in self._cards:
            print(f"{}"
