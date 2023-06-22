import prompt
from random import randint


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 200)
        print('Question: ' + str(random_number))
        answer = input('Your answer: ')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        elif random_number % 2 != 0:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f'\nLet\'s try again, {name}!')
            break
        i += 1
    print('Congratulations, ' + name + '!')
