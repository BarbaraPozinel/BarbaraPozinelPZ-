class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points,
    rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

lebron = BasketballPlayer(
    first_name="Lebron",
    last_name="James",
    height_cm=203,
    weight_kg=113,
    points=27.2,
    rebounds=7.4,
    assists=7.2
)

kev_dur = BasketballPlayer(
    first_name="Kevin",
    last_name="Durant",
    height_cm=210,
    weight_kg=108,
    points=27.2,
    rebounds=7.1,
    assists=4
)

print("Please enter basketball player's data:")
first_name1= input("Enter first name: ")
last_name1= input("Enter last name: ")
height1= input("Enter height in cm: ")
weight1= input("Enter weight in kg: ")
points1= input("Enter achieved points: ")
rebounds1 = input("Enter achieved rebounds: ")
assists1 = input("Enter assists: ")

new_player = BasketballPlayer(first_name=first_name1, last_name=last_name1, height_cm=height1, weight_kg=weight1, points=points1, rebounds=rebounds1, assists=assists1)

with open("basketballplayers.txt","w") as basketballplayers_file:
    basketballplayers_file.write(str(new_player.__dict__))

print("New player's data: {0}".format(new_player.__dict__) )


