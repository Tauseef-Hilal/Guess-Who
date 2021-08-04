"""
Classes.py
"""

from random import choice


class Card:
    """Defines a card"""

    def __init__(self, details_dict: dict) -> None:
        "Initialize card and set attributes"

        # Iterate over the keys of the dictionary and set instance attributes
        # with dict-keys as their names and dict-values as their values
        for key, value in details_dict.items():
            self.__setattr__(key, value)

    def __repr__(self) -> str:
        "Return the printable representation of a card"

        return f"{self.__class__.__name__}({vars(self)})"


class Player:
    """Model a player"""

    def __init__(self, questions: list, cards: list, human: bool) -> None:

        self.questions = questions
        self.cards = [Card(card) for card in cards]
        self.human = human

        if not self.human:
            self.name = "COMPUTER PLAYER"
            self.secret_card = choice(self.cards)
        else:
            self.name = "HUMAN PLAYER"

    def set_secret_card(self, name: str) -> bool:
        """
            Set secret card for the human player
        """

        for card in self.cards:
            if card.name == name.title():
                self.secret_card = card
                return True

        # Return False if there is no card named param: name
        return False

    def remove_question(self, id: int = 0) -> dict:
        """
            Remove the question with param: id from the cards attribute
        """
        if not isinstance(id, int):
            try:
                id = int(id)
            except ValueError:
                return {}

        if not self.human:
            return self.questions.pop(self.questions.index(
                choice(self.questions)))

        for question in self.questions:
            if question["id"] == id:
                return self.questions.pop(self.questions.index(question))

        # Return empty dict if there is no question with id = param: id
        return {}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{tuple(vars(self).keys())}"
