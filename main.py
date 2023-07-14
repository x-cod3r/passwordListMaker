import itertools

def generate_combinations(characters):
    combinations = []
    for r in range(1, len(characters) + 1):
        # Generate combinations of length r
        combos = itertools.combinations(characters, r)
        combinations.extend(combos)
    
    return combinations

# Prompt for input characters
input_characters = input("Enter characters (without spaces): ")

# Generate combinations
character_list = list(input_characters)
combinations = generate_combinations(character_list)

# Create and write combinations to a text file
filename = "combinations_output.txt"
with open(filename, "w") as file:
    file.write("All possible combinations:\n")
    for combo in combinations:
        file.write(''.join(combo) + "\n")

print("Combinations saved to", filename)
