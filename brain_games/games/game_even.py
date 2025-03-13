import random

#import prompt

# from brain_games.cli import welcome_user
# from brain_games.scripts.brain_games import greet

# MIN_NUMBER = 1
# MAX_NUMBER = 100

# ROUNDS_AMOUNT = 3

RULE = 'Answer "yes" if the number is even, otherwise answer "no".' 

def generate_round():
    number = random.randint(1, 100)
    is_even = number % 2 == 0
    
    question = str(number)
    
    right_answer = 'yes' if is_even else 'no'
    
    return question, right_answer