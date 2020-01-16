#Attempt to practice the randomization of the seat allocation & free Drink
import random

seat =["A1", "A2", "A3","A4","A5","A6","A6","A8","A9","A10","B1","B2","B3",\
"B4","B5","B6","B7","B8","B9","B10"]
#people who bought tickets
people = ["Jim","Wendy","Ken","Matt","Don","Dave","Sam","Chirs"]
#Drink on the seats
drink = ("Coke", "pepsi","beer","red wine")

random_seat = random.choice(seat)
seat.remove(random_seat)
random_people = random.choice(people)
people.remove(random_people)
random_drink = random.choice(drink)


print(f"{random_people} has been allocated seat number {random_seat},{random_drink} will be serve at your seat")
