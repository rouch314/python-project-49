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
     

# def main():

#     greet()
#     name = welcome_user()

#     print('What number is missing in the progression?')

#     for i in range(1, ROUNDS_AMOUNT + 1):
        
#         progression = []
            
#         random_number1 = random.randint(1, 20)
#         random_number2 = random.randint(1, 10)

#         result = random_number1

#         for _ in range(11):
#             result += random_number2
#             progression.append(result)             
            
#         hidden_index = random.randint(0, 10)
#         progression[hidden_index] = '..'
#         mapped_progression = ' '.join(map(str, progression))
    
#         if hidden_index == 0:
#             right_answer = progression[hidden_index + 1] 
#             - (progression[hidden_index + 2] 
#             - progression[hidden_index + 1])
#         elif hidden_index == 10:
#             right_answer = progression[hidden_index - 1] 
#             + (progression[hidden_index - 1] 
#             - progression[hidden_index - 2])
#         else:
#             right_answer = (progression[hidden_index + 1] 
#             + progression[hidden_index - 1]) / 2
        
#         print(f'Question: {mapped_progression}')

#         user_answer = int(prompt.string('Your answer: '))
        
#         if right_answer == user_answer:

#             print('Correct!')

#             i += 1 
#         elif right_answer != user_answer:
#             print(f'{user_answer} is wrong answer ;(.'
#                   f'Correct answer was {right_answer}. \n'
#                   f'Let`s try again, {name}!')
#             break
    
#         print(f'Congratulations, {name}!')
        

