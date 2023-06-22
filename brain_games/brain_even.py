from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even():
    random_number = randint(1, 200)
    print('Question: ' + str(random_number))
    answer = input('Your answer: ')
    if random_number % 2 == 0:
        correct_answer = 'yes'
    elif random_number % 2 != 0:
        correct_answer = 'no'
    return [answer, correct_answer]
