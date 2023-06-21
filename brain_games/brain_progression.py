import prompt
from random import randint
from random import choice


def brain_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
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
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.'
                  f'Let\'s try again, {name}!')
            break
        i += 1
    print('Congratulations, ' + name + '!')