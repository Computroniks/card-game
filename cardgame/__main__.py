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

def check(players: list[Collection.Hand]) -> list[tuple[int, int]]:
    """
    Check if each player has won or lost

    :param players: Array of players
    :type players: Collection.Hand
    :returns: Tuple containing the index and win state of each player.
        0 = lost, 1 = no change, 2 = won
    :rtype: list[tuple[int, int]]
    """

    card_vals = {
        1:1, 2:2,
        3:3, 4:4, 5:5,
        6:6, 7:7, 8:8,
        9:9, 10:10, 11:10,
        12:10, 13:10, 14:10
    }

    result = []

    for i in range(len(players)):
        total = 0
        for card in players[i].cards:
            total += card_vals[card.value]
        if total == 21
            result.append((i, 2))
            return result
        elif total < 21:
            result.append((i, 1))
        else:
            result.append((i, 0))
    return result

def parseResults(results: list[tuple[int, int]]) -> list[int]:
    """
    Parse results

    :param results: Results list
    :type results: list[tuple[int, int]]
    :rtype: list[int]
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

    results = check(players)
    del_list = []
    for result in results:
        if result[1] == 2:
            print(f"Player {result[0]+1} has won")
            return 0
        elif not result[1]:
            print(f"Player {result[0]+1} is out of the game")
            del_list.append(result[0])

    

    # Main game loop
    while True:
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
