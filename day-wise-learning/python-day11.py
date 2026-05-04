"""
Day 11 - Blackjack Capstone Project (Angela Yu)

GOAL:
Build a complete Blackjack game using:
- Functions
- Lists
- Loops
- Conditionals
- Random module

This is your FIRST real system-style program.

---------------------------------------------
🧠 SYSTEM DESIGN THINKING (IMPORTANT)

We break the game into modules:

1. deal_card()          -> handles card distribution
2. calculate_score()    -> business logic for score
3. compare()            -> result engine
4. play_game()          -> controller (main flow)

This is EXACTLY how backend systems are structured.

---------------------------------------------
🎴 GAME RULES (SIMPLIFIED)

- Cards: 2–10, Face cards = 10, Ace = 11 or 1
- Blackjack = Ace + 10 (returns 0 as special value)
- Player vs Computer
- Closest to 21 wins without exceeding

---------------------------------------------
"""

import random


# ---------------------------------------------
# 🎴 GLOBAL CARD DECK
# ---------------------------------------------
# 11 represents Ace (can later become 1 if needed)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# ---------------------------------------------
# 🎯 FUNCTION: DEAL A CARD
# ---------------------------------------------
def deal_card():
    """
    Returns a random card from the deck.
    Equivalent to Math.random() selection in JS.
    """
    return random.choice(cards)


# ---------------------------------------------
# 🧮 FUNCTION: CALCULATE SCORE
# ---------------------------------------------
def calculate_score(hand):
    """
    Takes a list of cards and returns score.

    SPECIAL RULES:
    - Blackjack (Ace + 10) → return 0 (sentinel value)
    - Ace adjustment: if total > 21, convert 11 → 1
    """

    # Blackjack condition
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    # Handle Ace (11 → 1)
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


# ---------------------------------------------
# ⚖️ FUNCTION: COMPARE SCORES
# ---------------------------------------------
def compare(user_score, computer_score):
    """
    Compares final scores and returns result string.
    Acts like a rules engine.
    """

    if user_score == computer_score:
        return "🤝 Draw"
    elif computer_score == 0:
        return "❌ Lose, opponent has Blackjack"
    elif user_score == 0:
        return "🔥 Win with Blackjack"
    elif user_score > 21:
        return "💥 You went over. You lose"
    elif computer_score > 21:
        return "🎉 Opponent went over. You win"
    elif user_score > computer_score:
        return "✅ You win"
    else:
        return "❌ You lose"


# ---------------------------------------------
# 🎮 FUNCTION: MAIN GAME CONTROLLER
# ---------------------------------------------
def play_game():
    """
    Controls full game flow.

    Responsibilities:
    - Initialize hands
    - Run player loop
    - Run dealer logic
    - Print results
    """

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initial deal (2 cards each)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # -----------------------------------------
    # 🔁 PLAYER LOOP
    # -----------------------------------------
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print("\n-----------------------------------")
        print(f"🧑 Your cards: {user_cards} | Score: {user_score}")
        print(f"💻 Computer's first card: {computer_cards[0]}")

        # Game end conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("👉 Type 'y' to draw another card, 'n' to stand: ")

            if choice.lower() == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # -----------------------------------------
    # 🤖 COMPUTER (DEALER) LOGIC
    # -----------------------------------------
    # Dealer draws until score >= 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # -----------------------------------------
    # 🏁 FINAL RESULT
    # -----------------------------------------
    print("\n=========== FINAL RESULT ===========")
    print(f"🧑 Your final hand: {user_cards} | Score: {user_score}")
    print(f"💻 Computer's final hand: {computer_cards} | Score: {computer_score}")

    print(compare(user_score, computer_score))


# ---------------------------------------------
# 🔁 GAME LOOP (REPLAY FEATURE)
# ---------------------------------------------
def start():
    """
    Allows user to play multiple rounds.
    """

    while True:
        print("\n🎮 Starting Blackjack Game...\n")
        play_game()

        again = input("\n🔁 Play again? (y/n): ")
        if again.lower() != 'y':
            print("👋 Thanks for playing!")
            break


# ---------------------------------------------
# 🚀 ENTRY POINT
# ---------------------------------------------
if __name__ == "__main__":
    start()


"""
---------------------------------------------
🚀 WHAT YOU BUILT (IMPORTANT)

- Modular system (like backend service)
- Game loop (like event loop / agent loop)
- Rule engine (compare function)
- State management (is_game_over)

---------------------------------------------
🧠 WHY THIS MATTERS FOR YOU

This is SAME thinking used in:

- AI Agents (loop + decision + state)
- RAG pipelines (steps + logic)
- Backend APIs (modular functions)

---------------------------------------------
🎯 NEXT STEP

Day 12 → Scope & Variable Rules (IMPORTANT for debugging + large systems)
---------------------------------------------
"""

