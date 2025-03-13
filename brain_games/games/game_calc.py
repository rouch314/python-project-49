import random

#import prompt

#from brain_games.cli import welcome_user
#from brain_games.scripts.brain_games import greet

# MIN_NUMBER = 1
# MAX_NUMBER = 100

#ROUNDS_AMOUNT = 3

RULE = 'What is the result of the expression?'

def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    
    question = f'{number1}{operator}{number2}'
    
    def calculate(num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2

    right_answer = calculate(number1, number2, operator)
    
    return question, right_answer

# def main():
#     greet()
#     name = welcome_user()

#     print('What is the result of the expression?')

#     operators_list = ['+', '-', '*']

#     for i in range(1, ROUNDS_AMOUNT + 1):
    
#         random_number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
#         random_number2 = random.randint(MIN_NUMBER, MAX_NUMBER)

#         random_operator = random.choice(operators_list)

#         def right_answer():
#             match random_operator:
#                 case '+': 
#                     return random_number1 + random_number2
#                 case '-': 
#                     return random_number1 - random_number2
#                 case '*': 
#                     return random_number1 * random_number2

#         print(f'Question: {random_number1}{random_operator}{random_number2}')

#         user_answer = int(prompt.string('Your answer: '))

#         if right_answer() == user_answer:
#             print('Correct!')
#             i += 1
#         elif right_answer() != user_answer:
#             print(f'{user_answer} is wrong answer ;(.'
#                   f'Correct answer was {right_answer}. \n'
#                   f'Let`s try again, {name}!')
#             break
#         print(f'Congratulations, {name}!')
