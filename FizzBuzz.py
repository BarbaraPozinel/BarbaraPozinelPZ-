print("Please select a number between 1 and 100:")
število = int(input())

for število in range (1,število+1):
    if število % 3 == 0 and število % 5 == 0:
        print("FizzBuzz")
    elif število % 3 == 0:
        print ("Fizz")
    elif število % 5 == 0:
        print ("Buzz")
    else:
        print(število)