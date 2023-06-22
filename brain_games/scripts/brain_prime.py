#!/usr/bin/python3
from brain_games.play_game import play_game
from brain_games.brain_prime import brain_prime
from brain_games.brain_prime import QUESTION


def main():
    play_game(QUESTION, brain_prime)


if __name__ == '__main__':
    main()
