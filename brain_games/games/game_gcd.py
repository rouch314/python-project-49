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
        

# def main():

#     greet()
#     name = welcome_user()

#     print('Find the greatest common divisor of given numbers.')

#     for i in range(1, ROUNDS_AMOUNT + 1):
#         random_number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
#         random_number2 = random.randint(MIN_NUMBER, MAX_NUMBER)

#         smallest_number = min(random_number1, random_number2)

#         def gcd():
#             for divisor in range(1, smallest_number + 1):
#                 if (random_number1 % divisor == 0 
#                         and random_number2 % divisor == 0):
#                     greatest_divisor = divisor
#                 divisor += 1
#             return greatest_divisor
        
#         print(f'Question: {random_number1} {random_number2}')

#         user_answer = int(prompt.string('Your answer: '))

#         if gcd() == user_answer:

#             print('Correct!')

#             i += 1 
#         elif gcd() != user_answer:
#             print(f'{user_answer} is wrong answer ;(.'
#                   f'Correct answer was {gcd}. \n'
#                   f'Let`s try again, {name}!')
#             break
    
#         print(f'Congratulations, {name}!')
