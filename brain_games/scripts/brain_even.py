#!/usr/bin/python3
from brain_games.play_game import play_game
from brain_games.brain_even import brain_even
from brain_games.brain_even import QUESTION


def main():
    play_game(QUESTION, brain_even)


if __name__ == '__main__':
    main()
