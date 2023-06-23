from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):
    count = 0
    for x in range(2, a):
        if a % x == 0:
            count += 1
    if count < 1:
        return True


def brain_prime():
    number = randint(0, 100)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
