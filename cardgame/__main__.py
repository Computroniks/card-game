# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import sys

import Card
import Collection

def getPlayers() -> int:
    """
    Get number of players in the game

    :rtype: int
    """

    while True:
        try:
            num = int(input("Please enter the number of players: "))
        except ValueError:
            print("Invalid number")
        if num > 0 and num < 5:
            return num
        else:
            print("Players must be in range 1-4")

def deal(deck: Collection.Deck, players: list[Collection.Hand], num_cards: int = 2) -> None:
    """
    Deal each player a set number of cards

    :param deck: Deck to deal from
    :type deck: Collection.Deck
    :param players: List of players to deal between
    :type players: list[Collection.Hand]
    :param num_cards: Number of cards to deal, defaults to 2
    :type num_cards: int, optional
    """
    
    for i in range(num_cards):
        for player in players:
            player.addCard(deck.pop())

def check(players: list[Collection.Hand]) -> list[tuple[int, bool]]:
    """
    """

def main() -> int:
    """
    Main entrypoint for game.

    :returns: 0 on success. Any other integer on error
    :rtype: int
    """
    
    deck = Collection.Deck(False)
    players = [Collection.Hand() for i in range(getPlayers())]
    deal(deck, players)

    # Main game loop
    while True:
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
