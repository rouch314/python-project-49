import random

# import prompt

# from brain_games.cli import welcome_user
# from brain_games.scripts.brain_games import greet

# MIN_NUMBER = 1
# MAX_NUMBER = 100

# ROUNDS_AMOUNT = 3

RULE = 'What is the result of the expression?'


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    
    question = f'{number1} {operator} {number2}'
    
    def calculate(num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2

    right_answer = calculate(number1, number2, operator)
    
    return question, right_answer
