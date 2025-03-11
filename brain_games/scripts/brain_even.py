import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet

MIN_NUMBER = 1
MAX_NUMBER = 100

ROUNDS_AMOUNT = 3


def main():

    greet()
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer"no".')

    for i in range(1, ROUNDS_AMOUNT + 1):
    
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        is_even = random_number % 2 == 0

        right_answer = 'yes' if is_even else 'no'

        print(f'Question: {random_number}')

        user_answer = prompt.string('Your answer: ')
            
        if right_answer == user_answer:

            print('Correct!')

            i += 1

        elif right_answer != user_answer:

            print('Wrong!')

            break

        if i == 3:
            print(f'Congratulations, {name}!')




