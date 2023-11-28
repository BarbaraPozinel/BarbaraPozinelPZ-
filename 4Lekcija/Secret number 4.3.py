import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0
ime = input("Vnesite ime: ")

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    print("Name: " + score_dict["name"] + ", secret number: " + score_dict["secret"])
    print("Wrong guesses: " + score_dict.get("wrong_guesses"))

sorted_dict = score_list.sort(key=lambda x: x["attempts"])
wrong_list = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": ime, "secret": str(secret), "wrong_guesses": str(wrong_list)})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
    wrong_list.append(guess)