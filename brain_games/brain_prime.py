from random import randint
from brain_games.functions import is_prime


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def brain_prime():
    a = randint(0, 100)
    print(f'Question: {a}')
    answer = input('Your answer: ')
    correct_answer = is_prime(a)
    return [answer, correct_answer]
