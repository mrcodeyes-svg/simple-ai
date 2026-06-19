import random
import json
import time
# 1. Training Data: The AI reads these real words to learn letter patterns
training_text = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape",'what','happy','no','abcdefghijklmnopqrstuvwxyz']

# 2. Build the AI's Probability Brain
# This dictionary tracks which letters frequently follow other letters
model_brain = {}
try:
    with open('brain.json', 'r') as f:
        model_brain = json.load(f)
        print(model_brain)
        time.sleep(3)

    with open('words.json', 'r') as f:
        stuff = json.load(f)
        training_text = set(stuff.keys())
except Exception:
    model_brain = {}

for word in training_text:
    # Add a start token and end token to learn how words begin and end
    spaced_word = "^" + word + "$"
    for i in range(len(spaced_word) - 1):
        current_letter = spaced_word[i]
        next_letter = spaced_word[i+1]
        
        if current_letter not in model_brain:
            model_brain[current_letter] = []
        if next_letter not in model_brain[current_letter]:
            model_brain[current_letter].append(next_letter)

# 3. Let the AI Generate Letters Permanently
# It runs entirely on its own with zero inputs
current = "^"  # Start token

print("--- Real AI Letter Stream Starting ---")
run = 0
while True:
    run += 1
    # Look at the current letter and pick the next logical letter based on training data
    if current in model_brain:
        possible_next_letters = model_brain[current]
        next_char = random.choice(possible_next_letters)
    else:
        next_char = "^"  # Reset if it hits a dead end
    if current not in model_brain:
            model_brain[current] = []
    if next_char not in model_brain[current]:
        model_brain[current].append(next)
        
    # If it generates an end token, print a space instead to separate "words"
    if next_char == "$":
        print(" ", end="", flush=True)
        current = "^"
    elif next_char == "^":
        current = "^"
    else:
        # Give out the letter
        print(next_char, end="", flush=True)
        current = next_char
    if run >= 1000:
        with open('brain.json', 'w') as f:
            json.dump(model_brain, f, indent=4)
            run = 0