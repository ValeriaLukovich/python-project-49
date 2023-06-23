#!/usr/bin/python3
from brain_games.play_game import play_game
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_calc import QUESTION


def main():
    play_game(QUESTION, brain_calc)


if __name__ == '__main__':
    main()
