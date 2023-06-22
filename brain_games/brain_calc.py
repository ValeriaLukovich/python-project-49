from random import randint
from random import choice
from brain_games.functions import which_sign
import prompt


def brain_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        a = randint(1, 20)
        b = randint(1, 20)
        sign = choice('+-*')
        expression = f'{a} {sign} {b}'
        print('Question: ' + expression)
        answer = int(input('Your answer: '))
        correct_answer = which_sign(a, b, sign)
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f'\nLet\'s try again, {name}!')
            break
        i += 1
    print('Congratulations, ' + name + '!')
