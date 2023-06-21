def is_prime(a):
    count = 0
    for x in range(2, a):
        if a % x == 0:
            count += 1
    if count < 1:
        return 'yes'
    else:
        return 'no'
