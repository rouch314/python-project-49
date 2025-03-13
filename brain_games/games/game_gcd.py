import random

# import prompt

# from brain_games.cli import welcome_user
# from brain_games.scripts.brain_games import greet

# MIN_NUMBER = 1
# MAX_NUMBER = 100

# ROUNDS_AMOUNT = 3

RULE = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)   
    
    question = f'{number1} {number2}'
    
    right_answer = gcd(number1, number2)
    
    return question, right_answer