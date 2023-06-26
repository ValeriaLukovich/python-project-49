#!/usr/bin/python3
from brain_games.play_game import play_game
from brain_games.games.brain_progression import get_question_and_answer
from brain_games.games.brain_progression import QUESTION


def main():
    play_game(QUESTION, get_question_and_answer)


if __name__ == '__main__':
    main()
