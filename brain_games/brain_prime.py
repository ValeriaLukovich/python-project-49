import prompt
from random import randint
from brain_games.functions import is_prime


def brain_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        a = randint(0, 100)
        print(f'Question: {a}')
        answer = input('Your answer: ')
        correct_answer = is_prime(a)
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.'
                  f'Let\'s try again, {name}!')
            break
        i += 1
    print('Congratulations, ' + name + '!')
