from operator import add
from operator import mul
from operator import sub


def which_sign(a, b, sign):
    if sign == '+':
        correct_answer = add(a, b)
    elif sign == '*':
        correct_answer = mul(a, b)
    elif sign == '-':
        correct_answer = sub(a, b)
    return correct_answer


def is_prime(a):
    count = 0
    for x in range(2, a):
        if a % x == 0:
            count += 1
    if count < 1:
        return 'yes'
    else:
        return 'no'
