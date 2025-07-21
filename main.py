import itertools
import random
import pandas as pd


# Generate participant IDs: P01 - P20
participants = [f"P{str(i+1).zfill(2)}" for i in range(20)]

# Generate condition names: Condition_1 - Condition_9
conditions = [f"Condition_{i+1}" for i in range(9)]

# List of 5 sentences
sentences = ["S1", "S2", "S3", "S4", "S5"]


# All possible sentence orders
all_permutations = list(itertools.permutations(sentences))

# Total number of combinations needed: 20 participants × 9 conditions = 180
permutations_needed = len(participants) * len(conditions)

# shuffle the list
random.shuffle(all_permutations)
permutations_list = (all_permutations * ((permutations_needed // len(all_permutations)) + 1))[:permutations_needed]


# Assign a sentence order for "participant ID - conditions name" pair
rows = []
index = 0
for participant in participants:
    for condition in conditions:
        sentence_order = permutations_list[index]
        rows.append({
            "Participant_ID": participant,
            "Condition": condition,
            "Sentence_Order": ", ".join(sentence_order)
        })
        index += 1


# Result: save to Excel
df = pd.DataFrame(rows)
df.to_excel("Sentence_Order_Assignment.xlsx", index=False)

# The sentence orders using an automated Python script
# based on balanced sampling from all possible sentence permutations (5! = 120 combinations) to minimise ordering bias.
print("saved as 'Sentence_Order_Assignment.xlsx'")