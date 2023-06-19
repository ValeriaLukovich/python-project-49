from random import randint
import prompt


def brain_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
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
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + str(correct_answer) + "'.\nLet's try again, " + name + "!")
            break
        i += 1


if __name__ == '__main__':
    brain_gcd()
