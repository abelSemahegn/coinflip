import random

def coin_flip():
    # Generate a random number (0 or 1)
    result = random.randint(0, 1)
    if result == 0:
        return "Heads"
    else:
        return "Tails"

# Test the function
print("Coin flip result:", coin_flip())

