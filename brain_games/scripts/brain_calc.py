from random import randint
from random import choice
import prompt


def brain_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        a = str(randint(1, 20))
        b = str(randint(1, 20))
        sign = choice('+-*')
        expression = a + ' ' + sign + ' ' + b
        print('Question: ' + expression)
        answer = int(input('Your answer: '))
        correct_answer = eval(a + sign + b)
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.\nLet\'s try again, {name}!')
            break
        i += 1
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    brain_calc()
