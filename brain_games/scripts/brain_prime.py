from random import randint
import prompt


def is_prime(a):
    count = 0
    for x in range(2, a):
        if a % x == 0:
            count += 1
    if count < 1:
        return 'yes'
    else:
        return 'no'


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
            print(f' \'{answer}\' is wrong answer ;(. Correct answer was \' {correct_answer}\'.\nLet\'s try again, {name}!')
            break
        i += 1


if __name__ == '__main__':
    brain_prime()
