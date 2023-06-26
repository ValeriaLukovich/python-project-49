import prompt


ROUNDS_AMOUNT = 3


def play_game(question, get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(question)
    round = 0
    while round < ROUNDS_AMOUNT:
        new_task, correct_answer = get_question_and_answer()
        print(f'Question: {new_task}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            round += 1
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f'\nLet\'s try again, {name}!')
            break
    if round == ROUNDS_AMOUNT:
        print('Congratulations, ' + name + '!')
