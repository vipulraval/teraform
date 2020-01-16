import random

bars = ["Hamilton",
        "1020 Bar",
        "Heights",
        "Dead Poet"]

people = ["Mattan",
          "that person you forgot to text back",
          "Glenn Hubbard",
          "Samuel L. Jackson",
          "John Keating"]

food = ["Waffle House",
        "Denny's",
        "Huddle House",
        "IHop",]

negative1 = ["Well, neither did I... I was just being polite.",
            "Oh well.",
            "Have fun being lame. I'm out!",
            "Good. I didn't want you to come anyway."]

random_bar = random.choice(bars)
random_person = random.choice(people)
people.remove(random_person)
random_person_1 = random.choice(people)
random_food = random.choice(food)
random_negative1 = random.choice(negative1)

print("We should go to a bar tonight.")
print("What do you think?")
answer = input("Enter yes or no: ")
if answer == "no":
    print(f"{random_negative1}")
if answer == "yes":
    print(f"Awesome! Well let's go to the {random_bar} around 9.")
    print(f"We should bring {random_person} and {random_person_1}.")
    print(f"I have a feeling that we may need to go to {random_food} afterwards.")
