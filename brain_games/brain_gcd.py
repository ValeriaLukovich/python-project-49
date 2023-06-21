import prompt
from random import randint


def brain_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        print('Question: ' + str(a) + ' ' + str(b))
        answer = input('Your answer: ')
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        correct_answer = str(a + b)
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.'
                  f'Let\'s try again, {name}!')
            break
        i += 1
    print('Congratulations, ' + name + '!')