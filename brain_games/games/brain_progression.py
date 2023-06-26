from random import randint


QUESTION = 'What number is missing in the progression?'


def get_question_and_answer():
    a = randint(0, 15)
    b = randint(1, 15)
    random_index = randint(0, 9)
    progression = list(range(a, 150, b))[:10]
    hidden_number = progression[random_index]
    progression[random_index] = '..'
    new_task = ' '.join(map(str, progression))
    correct_answer = str(hidden_number)
    return new_task, correct_answer
