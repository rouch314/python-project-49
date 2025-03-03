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

    print('What is the result of the expression?')

    operators_list = ['+', '-', '*']

    for i in range(1, ROUNDS_AMOUNT + 1):
    
        random_number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_number2 = random.randint(MIN_NUMBER, MAX_NUMBER)

        random_operator = random.choice(operators_list)

        def right_answer():
            match random_operator:
                case '+': return random_number1 + random_number2
                case '-': return random_number1 - random_number2
                case '*': return random_number1 * random_number2

        print(f'Question: {random_number1}{random_operator}{random_number2}')

        user_answer = int(prompt.string('Your answer: '))

        if right_answer() == user_answer:
            print('Correct!')
            i += 1
        elif right_answer() != user_answer:
                print(f'{user_answer} is wrong answer ;(. Correct answer was {right_answer()}. \nLet`s try again, {name}!')
                break


        print(f'Congratulations, {name}!')