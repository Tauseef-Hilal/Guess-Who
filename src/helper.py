"""
    Contains some functions required by other modules
"""
import sys
import os
import json
from os import system
from time import sleep
from .display import LINE
from .classes import Player

##################################################################
# Import cards from cards.json and questions from questions.json
##################################################################
try:
    with open("Data/cards.json") as cards_json:
        cards_list = json.load(cards_json)

    with open("Data/questions.json") as questions_json:
        questions_list = json.load(questions_json)
except FileNotFoundError:
    print(LINE)
    print(f"{' '*70}[ERROR] Missing file(s) in ./Data directory.")
    print(f"{' '*75}Try downloading the repo again!")
    input(LINE)
    sys.exit()
##################################################################


def create_players():
    """
        Create Player objects
    """
    computer_player = Player(questions=questions_list[:],
                             cards=cards_list[:],
                             human=False)
    human_player = Player(questions=questions_list[:],
                          cards=cards_list[:],
                          human=True)

    return computer_player, human_player


def pick_card(human_player):
    """
        Set secret card for human player
    """
    while True:
        card_name = input(">>> Pick a card :: (name) :: ")
        card_set = human_player.set_secret_card(card_name)

        if not card_set:
            print("Invalid option!")
            continue
        break


def pick_question(human_player):
    """
        Pick question from human player's list
    """
    while True:
        question_id = input(">>> Pick a question :: (id : number) :: ")
        question = human_player.remove_question(question_id)

        if not question:
            print("Invalid option!")
            continue
        break

    return question


def ask_question(player):
    """
        Returns a random question if player is not human
        else func pick_question is called
    """
    return pick_question(player) if player.human else player.remove_question()


def get_human_res(question):
    """
        Get response from human player
    """
    print(f"{LINE}\n[*] Computer's question: {question['question']}")
    while True:
        try:
            res = input(">>> [Yes(Y) | No(N)]: ")[0].lower()
        except ValueError:
            pass

        if res not in ("y", "n"):
            print("Invalid answer!")
            continue
        break

    return res == "y"


def get_player_res(player, question):
    """
        Get player's response
    """
    if player.human:
        res = get_human_res(question)
    else:
        attr, value = question["attr"], question["value"]

        if "-" in attr:
            sep = "-"
            if "-of-" in attr:
                sep = "-of-"

            card_attr, dict_key = attr.split(sep)
            res = vars(player.secret_card)[card_attr].get(dict_key) == value

        else:
            res = vars(player.secret_card)[attr] == value

    return res


def remove_cards(player, player_res, question_value, card_attr, dict_key=None):
    """
        Remove cards from questioners list based on other player's response
    """

    remaining = []
    for card in player.cards:
        if player_res:
            if dict_key:
                if vars(card)[card_attr].get(dict_key) == question_value:
                    remaining.append(card)
            elif vars(card)[card_attr] == question_value:
                remaining.append(card)
        else:
            if dict_key:
                if vars(card)[card_attr].get(dict_key) != question_value:
                    remaining.append(card)
            elif vars(card)[card_attr] != question_value:
                remaining.append(card)

    player.cards = remaining


def handle_question(questioner, answerer, question):
    """
        Handle question
    """
    # Get player's response to the asked question
    player_res = get_player_res(answerer, question)

    # Remove cards based on response
    attr, value = question["attr"], question["value"]
    card_attr, dict_key = attr, None

    if "-" in attr:
        sep = "-"
        if "-of-" in attr:
            sep = "-of-"

        card_attr, dict_key = attr.split(sep)

    remove_cards(questioner, player_res, value, card_attr, dict_key)


def exit_game() -> None:
    """
        Exit the game!
    """

    print(f"{LINE}\n\t\t\t\t\t\t\t\t\t|Thanks for playing!|\n{LINE}")
    sleep(0.4)
    sys.exit()


def clear_screen() -> int:
    """
        This function uses the system function from os to
        clear the console screen. It passes 'clear' or 'cls'
        as the arguments depending on the OS.
    """

    return system("cls") if os.name == "nt" else system("clear")
