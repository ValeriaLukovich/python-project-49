from random import randint
from random import choice
import prompt

def brain_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        a = randint(0, 15)
        b = randint(1, 15)
        string = list(range(a, 150, b))[:10]
        correct_answer = choice(string)
        for index, char in enumerate(string):
            if char == correct_answer:
                string[index] = '..'
        new_string = ' '.join(map(str, string))
        print(f' Question: {new_string}')
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        elif answer != str(correct_answer):
            print(f' \'{answer}\' is wrong answer ;(. Correct answer was \' {correct_answer}\'.\nLet\'s try again, {name}!')
            break
        i += 1
if __name__ == '__main__':
    brain_progression()
