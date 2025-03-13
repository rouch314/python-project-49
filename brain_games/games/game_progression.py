import random

# import prompt

# from brain_games.cli import welcome_user
# from brain_games.scripts.brain_games import greet

# MIN_NUMBER = 1
# MAX_NUMBER = 100

# ROUNDS_AMOUNT = 3

RULE = 'What number is missing in the progression?'

def generate_progression(start, step, length = 10):
    return [start + step * i for i in range(length)]

def generate_round():
    begin = random.randint(1, 20)
    step = random.randint(1, 10)
    length = 10
    
    progression = generate_progression(begin, step, length)
    hidden_index = random.randint(0, length - 1)
    right_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    
    question = ' '.join(map(str, progression))
    return question, right_answer