import prompt


def play_game(question, function):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(question)
    round = 0
    win = 0
    while round < 3:
        list = function()
        if list[0] == list[1]:
            print('Correct!')
            win += 1
            round += 1
        elif list[0] != list[1]:
            print(f'\'{list[0]}\' is wrong answer ;(. '
                  f'Correct answer was \'{list[1]}\'.'
                  f'\nLet\'s try again, {name}!')
            break
    if win == 3:
        print('Congratulations, ' + name + '!')
