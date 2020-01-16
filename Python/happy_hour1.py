import random

bars = ["The Hamilton",
        "1020 Bar",
        "The Heights",
        "The Dead Poet"]

people = ["Mattan",
          "that person you forgot to text back",
          "Glenn Hubbard",
          "vipul raval",
          "Samuel L. Jackson"]
negative = ["well then go to hell",
            "how about we go to beach",
            "let's go home"]

random_bar = random.choice(bars)
random_people = random.choice(people)

print (f"i will be going to the bar {random_bar} with {random_people}")
