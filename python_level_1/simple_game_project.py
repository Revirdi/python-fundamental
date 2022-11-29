# The computer will think of 3 digit number that has no repeating digits
# You will then guuess a 3 digit number
# The computer will then give back clues.
# Based on these clues you will guess again until you break the code with a match!

# Close : You've guessed a correct number but in the wrong position
# Match: You've guessed a correct number in the correct position
# Nope: You haven't guess any of the numbers correctly

import random

# Get Guess
def get_guess():
    return list(input("What is your guess : "))

# Generate Computer Code
def generate_code():
    digits = [str(num) for num in range(10)]
    # Shuffle the digits
    random.shuffle(digits)
    # grab the first 3 digits
    return digits[:3]

# Generate The Clues
def generate_clues(code, user_guess):

    if user_guess==code:
        return "CODE CRACKED!"
    
    clues = []

    for idx,num in enumerate(user_guess):
        if num == code[idx]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    
    if clues == []:
        return ["Nope"]
    else:
        return clues

# Run Game Logic
print("Welcome Code Breaker!")

secret_code = generate_code()
clue_report = []

while clue_report != "CODE CRACKED!":

    guess = get_guess()

    clue_report = generate_clues(secret_code, guess)
    for clue in clue_report:
        print(clue)

    