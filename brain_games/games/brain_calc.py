from random import randint
from random import choice
from operator import add
from operator import mul
from operator import sub


QUESTION = 'What is the result of the expression?'


def find_operation(sign):
    if sign == '+':
        return add
    elif sign == '*':
        return mul
    elif sign == '-':
        return sub


def get_question_and_answer():
    a = randint(1, 20)
    b = randint(1, 20)
    sign = choice('+-*')
    new_task = f'{a} {sign} {b}'
    correct_answer = str(find_operation(sign)(a, b))
    return new_task, correct_answer
