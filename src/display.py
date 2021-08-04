"""
    Contains display-specific functions
"""

LINE = "=" * 175

MENU = """
{}
\t\t\t\t\t\t\t\t\t\t[GUESS WHO]\t\t\t\t\t\t\t\t\t\t[v0.01]
{}
\t\t\t\t\t\t\t\t\t     [1] {}
\t\t\t\t\t\t\t\t\t     [2] About Game
\t\t\t\t\t\t\t\t\t     [3] Credits
\t\t\t\t\t\t\t\t\t     [4] Quit
{}"""

CREDITS = f"""
{LINE}
\t\t\t\t\t\t\t\t\t\t[CREDITS]
{LINE}
\t\t\t\t\t\t\t\t  Currently there is nothing in here!
{LINE}"""

ABOUT = f"""
{LINE}
\t\t\t\t\t\t\t\t\t\t[ABOUT]
{LINE}
\t\t\t\t\t\t\t\t  Currently there is nothing in here!
{LINE}"""


def show_questions(player):
    """
        Display available questions of player
    """
    print(LINE)
    print(f"{' '*70}[HUMAN PLAYER'S AVAILABLE QUESTIONS]{' '*75}")
    print(LINE)
    for question in player.questions:
        print(f"[{question['id']}] {question['question']}")
    print(LINE)


def show_cards(player):
    """
        Display available cards of player
    """
    print(LINE)
    print(f"{' '*73}[HUMAN PLAYER'S AVAILABLE CARDS]{' '*75}")
    print(LINE)
    print(*player.cards, sep="\n")
    print(LINE)
    if player.human:
        print(
            f"{''*77}[SECRET CARD] -> {vars(player.secret_card)}")
        print(LINE)


def game_over_screen(human_player, winner):
    """
        Show game over screen
    """
    print(LINE)
    if winner == human_player:
        print(f"{' '*82}CONGRATULATIONS!")
        print(f"{' '*85}YOU WON!")
    else:
        print(f"{' '*79}BETTER LUCK NEXT TIME!")
        print(f"{' '*83}COMPUTER WINS!")
    print(LINE)


def show_menu(first_option) -> None:
    """
        Display the home page

    """

    print(MENU.format(LINE, LINE, first_option, LINE))


def show_about_page() -> None:
    """
        Display the about page
    """

    print(ABOUT)
    input()


def show_credits_page() -> None:
    """
        Display the credits page
    """

    print(CREDITS)
    input()
