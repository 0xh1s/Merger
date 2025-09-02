from itertools import permutations, product

# --- CONFIGURATION ---
words = ["wade", "watts"]  # Add the words to merge
use_uppercase = True       # True to include uppercase, False for lowercase only
# ---------------------

# Combine all letters in the original order (keeping repetitions)
letters = list("".join(words))

# Exact length: depends on how many letters are in total
length = len(letters)

result = set()

def apply_uppercase(word):
    """Generates all possible uppercase/lowercase combinations for a given word."""
    return { "".join(combo) for combo in product(*[(c.lower(), c.upper()) for c in word]) }

# Generate unique permutations keeping exact repetitions
for p in set(permutations(letters, length)):
    word = "".join(p)
    if use_uppercase:
        result.update(apply_uppercase(word))
    else:
        result.add(word)

# Save to file
with open("dictionary.txt", "w") as f:
    for word in sorted(result):
        f.write(word + "\n")

print(f"[+] Dictionary generated with {len(result)} combinations in dictionary.txt")