import random
import prompt
from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user

MIN_NUMBER = 1
MAX_NUMBER = 100

ROUNDS_AMOUNT = 3


def main():

    greet()
    name = welcome_user()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(1, ROUNDS_AMOUNT + 1):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        divisors = []
        right_answer = 'no'
        
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                divisors.append(divisor)
        if len(divisors) == 2:
            right_answer = 'yes'
        
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        
        if right_answer == user_answer:
           print('Correct!')
           i += 1
        elif right_answer != user_answer:
                print(f'{user_answer} is wrong answer ;(. Correct answer was {right_answer}. \nLet`s try again, {name}!')
                break
        if i == 4:
            print(f'Congratulations, {name}!')            

             
    