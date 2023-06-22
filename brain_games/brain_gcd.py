from random import randint

QUESTION = 'Find the greatest common divisor of given numbers.'


def brain_gcd():
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
    return [answer, correct_answer]
