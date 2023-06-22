from random import randint
from random import choice
from brain_games.functions import which_sign


QUESTION = 'What is the result of the expression?'


def brain_calc():
    a = randint(1, 20)
    b = randint(1, 20)
    sign = choice('+-*')
    expression = f'{a} {sign} {b}'
    print('Question: ' + expression)
    answer = int(input('Your answer: '))
    correct_answer = which_sign(a, b, sign)
    return [answer, correct_answer]
