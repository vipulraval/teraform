import random

bars = ["The Hamilton",
        "1020 Bar",
        "The Heights",
        "The Dead Poet"]

people = ["Mattan",
          "that person you forgot to text back",
          "Glenn Hubbard",
          "Vipul Raval",
          "Samuel L. Jackson"]

random_bar = random.choice(bars)
random_person = random.choice(people)
people.remove(random_person)

print(f"How about you go to {random_bar} with {random_person}?")
