from random import randint
from random import choice
import prompt
from operator import add
from operator import mul
from operator import sub


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
        expression = f'{a}{ sign}{ b}'
        print('Question: ' + expression)
        answer = int(input('Your answer: '))
        if sign == '+':
            correct_answer = add(a, b)
        elif sign == '*':
            correct_answer = mul(a, b)
        elif sign == '-':
            correct_answer = sub(a, b)
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.'
                  f'Let\'s try again, {name}!')
            break
        i += 1
    print('Congratulations, ' + name + '!')
