#!/usr/bin/python3
from brain_games.play_game import play_game
from brain_games.brain_progression import brain_progression
from brain_games.brain_progression import QUESTION


def main():
    play_game(QUESTION, brain_progression)


if __name__ == '__main__':
    main()
