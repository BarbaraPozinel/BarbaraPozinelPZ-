import datetime
import json
import random

def play_game(level = "X"):
    secret = random.randint(1, 30)
    attempts = 0
    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        score_list = get_score_list()

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret and level == "X":
            print("Your guess is not correct... try something smaller")
        elif guess < secret and level == "X":
            print("Your guess is not correct... try something bigger")

def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list

while True:
    choice = input("Would you like to A) Play a new game? B) see the best scores? C) End game? Input A/B/C: ")
    if choice == "A":
        choice2 = input("Would you like X) Easy level? or Y) Hard level? Input X/Y: ")
        if choice2 == "X":
            play_game(level="X")
        else:
            play_game(level="Y")
    if choice == "B":
        print("Top scores " + str(get_top_scores())+ str("\n"))
    if choice == "C":
        break