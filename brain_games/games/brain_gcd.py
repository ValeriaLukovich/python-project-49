from random import randint
from math import gcd

QUESTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    a = randint(1, 100)
    b = randint(1, 100)
    new_task = str(a) + ' ' + str(b)
    correct_answer = str(gcd(a, b))
    return new_task, correct_answer
