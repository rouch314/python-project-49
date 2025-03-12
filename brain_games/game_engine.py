import prompt

ROUNDS_AMOUNT = 3

def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!\n{game.RULE}')
    
    for _ in range(ROUNDS_AMOUNT):
        question, right_answer = game.generate_round()
        print(f'Question:{question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer != str(right_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print('Correct!')
        
    print(f'Congratulations, {name}!')
    