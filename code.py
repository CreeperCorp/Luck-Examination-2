import random

def roll_score():
    score = random.randint(400, 1600)
    print(f"Random Roll: You scored {score} points!")
    return score

def guess_number_score(game_num, max_points):
    number = random.randint(1, 10)
    try:
        guess = int(input(f"Guessing Game {game_num}: Guess a number between 1 and 10: "))
    except ValueError:
        guess = -1  # Bad input
    if guess == number:
        score = max_points
        print("Amazing! You guessed correctly.")
    elif abs(guess - number) == 1:
        score = int(max_points * 0.75)
        print(f"So close! The number was {number}.")
    else:
        score = int(max_points * 0.5)
        print(f"Not quite. The number was {number}.")
    print(f"Guessing Game {game_num}: You scored {score} points!")
    return score

def coin_flip_score():
    flip = random.choice(['heads', 'tails'])
    guess = input("Guess the coin flip (heads or tails): ").strip().lower()
    if guess == flip:
        score = 1600
        print(f"Correct! It was {flip}.")
    else:
        score = 800
        print(f"Wrong! It was {flip}.")
    print(f"Coin Flip: You scored {score} points!")
    return score

def grade_from_score(total_score, max_score):
    percent = total_score / max_score
    if percent >= 0.94:
        return 'A+'
    elif percent >= 0.88:
        return 'A'
    elif percent >= 0.81:
        return 'B+'
    elif percent >= 0.75:
        return 'B'
    elif percent >= 0.69:
        return 'C+'
    elif percent >= 0.62:
        return 'C'
    elif percent >= 0.56:
        return 'D'
    else:
        return 'F'

def main():
    print("Welcome to Luck Examination 2!")
    print("You will play several games, and your scores will be added up and graded like the SAT.")
    print("-" * 50)

    total_score = 0
    max_score = 1600 * 3  # 1600 each for roll, coin, and all guessing games

    # Game 1: Random Roll
    total_score += roll_score()
    print("-" * 50)

    # Game 2: Coin Flip
    total_score += coin_flip_score()
    print("-" * 50)

    # Games 3–5: Guess the Number (combined 1600 points)
    guess_games = 3
    guess_points = [533, 533, 534]  # Sums to 1600
    for i in range(guess_games):
        total_score += guess_number_score(i + 1, guess_points[i])
        print("-" * 50)

    print(f"Your total Luck Score is: {total_score} out of {max_score}")
    grade = grade_from_score(total_score, max_score)
    print(f"Equivalent Grade: {grade}")

if __name__ == "__main__":
    main()
