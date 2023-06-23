#!/usr/bin/python3
from brain_games.play_game import play_game
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.brain_gcd import QUESTION


def main():
    play_game(QUESTION, brain_gcd)


if __name__ == '__main__':
    main()
