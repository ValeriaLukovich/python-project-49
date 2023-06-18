#!/usr/bin/env python3
from random import randint
import prompt


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 200)
        print('Question: ' + str(random_number))
        answer = input('Your answer: ')
        if (answer == 'yes' and random_number % 2 == 0) or (answer == 'no' and random_number % 2 != 0):
            print('Correct!')
        elif (answer == 'yes' and random_number % 2 != 0) or (answer != 'yes' and random_number % 2 != 0):
            print("'" + answer + "' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name + "!")
            break
        elif (answer == 'no' and random_number % 2 == 0) or (answer != 'no' and random_number % 2 == 0):
            print("'" + answer + "' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + name + "!")
            break
        i += 1
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    brain_even()
