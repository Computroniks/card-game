# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT


class Card:
    def __init__(self, suit: str = "hearts", value: int = 1) -> None:
        """
        Class that represents cards

        :param suit: The suit the card belongs to, defaults to "hearts"
        :type suit: str, optional
        :param value: Value card holds. Note: Ace is 1 or 14, King is 13,
            Queen is 12 and Jack 11, defaults to 1
        :type value: int, optional
        """
        
        self._suit = None
        self._value = value
        self._color = None
        self.suit = suit
        self._visible = False

    @property
    def suit(self) -> str:
        """
        The cards suit

        :rtype: str
        """
        
        return self._suit

    @suit.setter
    def suit(self, value: str) -> None:
        """
        Setter for suit

        Validates input

        :param value: Value to set - one of "hearts", "dimonds", "clubs"
            or "spades"
        :type value: str
        :raises ValueError: The supplied value was not a valid option
        """
        
        valid = ["hearts", "dimonds", "clubs", "spades"]
        value = value.lower()

        if value in valid:
            self._suit = value
            if value == "hearts" or value == "dimonds":
                self._color = "red"
            else:
                self._color = "black"
        else:
            raise ValueError

    @property
    def value(self) -> int:
        """
        Integer representation of the value

        An integer representation of the cards value where Ace is 1 or 14,
            King is 13, Queen is 12 and Jack is 11

        :rtype: int
        """
        
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        """
        Set value of value

        Checks if value is in range 1-14 inclusive and sets value

        :param value: Value to set. Must be in range 1-14 inclusive
        :type value: int
        :raises ValueError: The provided value is invalid
        """
        
        if int(value) <= 14 and int(value) >= 1:
            self._value = int(value)
        else:
            raise ValueError

    @property
    def color(self) -> str:
        """
        Representation of color of card

        :returns: One of "black" or "red"
        :rtype: str
        """
        
        return self._color

    @property
    def visible(self) -> bool:
        """
        Is this card visible to all?

        :rtype: bool
        """

        return self._visible

    def show(self) -> None:
        """Show this card"""

        self._visible = True

    def hide(self) -> None:
        """Hide this card"""

        self._visible = False

    def toggleVisible(self) -> None:
        """Toggle the visibility of the card"""

        self._visible = not self._visible

    def getParsedValue(self) -> str:
        """
        Get the human readable version of the cards value

        :rtype: str
        """

        special_cards = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace",
        }

        if self._value > 1 and self._value < 11:
            return str(self._value)
        else:
            return special_cards[self._value]
            
