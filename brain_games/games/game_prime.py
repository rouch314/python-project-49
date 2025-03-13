import random
# import prompt
# from brain_games.scripts.brain_games import greet
# from brain_games.cli import welcome_user

# MIN_NUMBER = 1
# MAX_NUMBER = 100

# ROUNDS_AMOUNT = 3

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num + 1)):
        if num % divisor == 0:
            return False
    return True

def generate_round():
    number = random.randint(2, 100)
    question = str(number)
    right_answer = 'yes' if is_prime(number) else 'no'
    
    return question, right_answer

    