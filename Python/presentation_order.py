import random

presenters = ["John", "Danielle", "Kara", "Tom", "Sally"]

p1 = random.choice(presenters)
presenters.remove(p1)

p2 = random.choice(presenters)
presenters.remove(p2)

p3 = random.choice(presenters)
presenters.remove(p3)

p4 = random.choice(presenters)
presenters.remove(p4)

p5 = random.choice(presenters)

print(f"The presentations will start with {p1}, followed by {p2}, {p3}, {p4}, and closing with {p5}.")
