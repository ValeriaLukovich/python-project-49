from random import randint
from random import choice


QUESTION = 'What number is missing in the progression?'


def brain_progression():
    a = randint(0, 15)
    b = randint(1, 15)
    string = list(range(a, 150, b))[:10]
    hidden_number = choice(string)
    for index, char in enumerate(string):
        if char == hidden_number:
            string[index] = '..'
    new_string = ' '.join(map(str, string))
    print(f' Question: {new_string}')
    answer = input('Your answer: ')
    correct_answer = str(hidden_number)
    return [answer, correct_answer]
