import prompt


def welcome_user():
    user_name = prompt.string('May I have your precious name? ')
    print(f'Hello, {user_name}!')