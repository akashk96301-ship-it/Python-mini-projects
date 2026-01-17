import random

def generate_number():
    return random.randint(1,100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Enter a number only.")

def check_guess(secret_number, guess):
    if guess > secret_number:
        return "Too High"
    elif guess < secret_number:
        return "Too Low"
    else:
        return "Correct"
    
def play_game():
    secret_number = generate_number()
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True:
        guess = get_user_guess()
        attempts += 1

        result = check_guess(secret_number, guess)
        print(result)

        if result == "Correct":
            print(f"Congratulation! You guessed the numberin {attempts} attempts ")
            break

play_game()