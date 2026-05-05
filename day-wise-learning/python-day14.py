# Day 14 - Higher Lower Game

import random
import os

# Sample dataset (in course this comes from game_data.py)
data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician",
        "country": "USA"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor",
        "country": "USA"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 174,
        "description": "Musician",
        "country": "USA"
    }
]

# Format account data for display
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Compare follower count
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Clear screen (optional)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Game logic
def game():
    score = 0
    game_should_continue = True

    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        # Avoid same comparison
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print("VS")
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_correct = check_answer(guess, a_followers, b_followers)

        clear()

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Wrong. Final score: {score}")


# Run game
game()