import random

flip = random.randint(1, 2)

if flip == 1:
    print("Heads!", end="", flush=True)
else:
    print("Tails!", end="", flush=True)

