
while True:
    print("Would you like to continue? Answer yes or no.")
    choice = input().lower()
    if choice == "yes":
        print("Good let's move on!")
    elif choice == "no":
        print("Okay. Don't forget to logout.")
        break
    else:
        print("The input is incorrect. Try again.")
