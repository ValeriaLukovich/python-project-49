from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def get_question_and_answer():
    random_number = randint(1, 200)
    if is_even(random_number):
        result = 'yes'
    else:
        result = 'no'
    return random_number, result
