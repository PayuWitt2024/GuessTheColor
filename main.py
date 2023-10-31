import random

COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
CODE_LENGTH = 4

def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def get_feedback(guess, code):
    feedback = {'black': 0, 'white': 0}
    code_copy = code.copy()  # Make a copy to avoid modifying the original list
    # Check for black pegs (count of 'correct color in correct position')
    for i in range(len(guess)):
        if guess[i] == code[i]:
            feedback['black'] += 1
            code_copy[i] = None  # Mark to avoid re-matching
    # Check for white pegs (count of 'correct color in wrong position')
    for i in range(len(guess)):
        if guess[i] in code_copy and guess[i] != code[i]:
            feedback['white'] += 1
            code_copy[code_copy.index(guess[i])] = None  # Mark to avoid re-matching
    return feedback

def mastermind_game():
    print("Welcome to Mastermind!")
    secret_code = generate_code()
    attempts = 10

    print("Available colors:", ', '.join(COLORS))

    while attempts > 0:
        guess = input(f"Enter your guess (e.g., red blue green yellow): ").lower().split()
        
        if len(guess) != CODE_LENGTH or not all(color in COLORS for color in guess):
            print(f"Please enter a sequence of {CODE_LENGTH} valid colors.")
            continue

        feedback = get_feedback(guess, secret_code)
        print(f"Black pegs: {feedback['black']}, White pegs: {feedback['white']}")

        if feedback['black'] == CODE_LENGTH:
            print("Congratulations! You've guessed the code!")
            break
        
        attempts -= 1
        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The code was: {' '.join(secret_code)}")

mastermind_game()
