"""
    Title: Guess Who [Human VS Computer]
    Contributors: Check on GitHub

    Guess Who? is a classic fun game for two players.
"""

from time import sleep
from random import choice
from .display import (LINE,
                      show_cards,
                      show_questions,
                      game_over_screen,
                      show_menu,
                      show_about_page,
                      show_credits_page)

from .helper import (ask_question,
                     handle_question,
                     create_players,
                     pick_card,
                     clear_screen,
                     exit_game)


def start_game():
    """
        Handle the game
    """
    # Create Player objects
    computer_player, human_player = create_players()
    players = [computer_player, human_player]

    # Display computer player's cards and set human player's secret card
    show_cards(computer_player)
    pick_card(human_player)

    current_player = choice(players)
    other_player = players[1 if current_player == computer_player else 0]

    winner = None
    game_over = False
    while not game_over:
        # Clear screen
        clear_screen()

        # Display human player's available cards and questions
        show_cards(human_player)
        print(f"{' '*77}[{current_player.name}'S TURN]{' '*75}")
        if current_player == human_player:
            show_questions(current_player)

        # Ask and handle a question
        question = ask_question(current_player)
        handle_question(questioner=current_player,
                        answerer=other_player,
                        question=question)

        if len(current_player.cards) == 1:
            winner = current_player
            game_over = True
        else:
            current_player, other_player = other_player, current_player

    game_over_screen(human_player, winner)
    input()


def main() -> None:
    """Main function"""

    first_option = "Start Game"
    funcs = [start_game,
             show_about_page,
             show_credits_page,
             exit_game]

    while True:
        clear_screen()
        show_menu(first_option=first_option)
        option = input("Choose an option >>> ")

        if option in ("1", "2", "3", "4"):

            # If player chose the first option, modify the first option of
            # the menu screen to show 'Play Again' instead of 'Start Game'.
            # This saves us from creating 'play_again' function!
            if option == "1":
                first_option = "Play Again"

            # Clear screen and call the desired function
            clear_screen()
            funcs[int(option) - 1]()

        else:
            print(f"Invalid Option!\n{LINE}")
            sleep(0.4)


if __name__ == "__main__":
    main()
