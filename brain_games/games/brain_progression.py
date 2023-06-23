from random import randint
from random import choice


QUESTION = 'What number is missing in the progression?'


def brain_progression():
    a = randint(0, 15)
    b = randint(1, 15)
    progression = list(range(a, 150, b))[:10]
    hidden_number = choice(progression)
    i = progression.index(hidden_number)
    progression[i] = '..'
    new_task = ' '.join(map(str, progression))
    correct_answer = str(hidden_number)
    return new_task, correct_answer
