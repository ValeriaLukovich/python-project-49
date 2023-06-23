from random import randint
from random import choice
from operator import add
from operator import mul
from operator import sub


QUESTION = 'What is the result of the expression?'


def operation(a, b, sign):
    if sign == '+':
        correct_answer = add(a, b)
    elif sign == '*':
        correct_answer = mul(a, b)
    elif sign == '-':
        correct_answer = sub(a, b)
    return correct_answer


def brain_calc():
    a = randint(1, 20)
    b = randint(1, 20)
    sign = choice('+-*')
    new_task = f'{a} {sign} {b}'
    correct_answer = str(operation(a, b, sign))
    return new_task, correct_answer
