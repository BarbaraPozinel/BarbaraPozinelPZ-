import datetime
import json
import random

class Result():
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date

def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    name = input("Enter your name: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        score_list = get_score_list()

        if guess == secret:
            result_obj = Result(score = attempts, player_name= name, date= str(datetime.datetime.now()))
            score_list.append(result_obj.__dict__)

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k["score"])[:3]
    return top_score_list

while True:
    choice = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if choice == "A":
        play_game()
    elif choice == "B":
        print("Top scores " + str(get_top_scores()) + str("\n"))
    else:
        break