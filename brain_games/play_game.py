import prompt


def play_game(question, function):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(question)
    round = 0
    win = 0
    while round < 3:
        new_task, correct_answer = function()
        print(f'Question: {new_task}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            win += 1
            round += 1
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f'\nLet\'s try again, {name}!')
            break
    if win == 3:
        print('Congratulations, ' + name + '!')
