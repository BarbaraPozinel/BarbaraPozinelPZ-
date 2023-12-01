import random

capitals = {"Črna Gora": "Podgorica", "Slovaška": "Bratislava", "Hrvaška": "Zagreb", "Belorusija": "Minsk", "Latvija": "Riga", "Slovenija": "Ljubljana", "Ukrajina": "Kijev"}

country = random.choice(list(capitals.keys()))

guess = input("What is the capital city of " + str(country) + "? ").lower()

if guess == capitals[country].lower():
    print("You've guessed it!")
else:
    print("Wrong. Try again.")
