import random
import math

dice = (1, 2, 3, 4, 5, 6)
tries = 0
numbers = 6
first_round = []
total_sum = 0

collection = []
score = {
    "1D": 0,
    "2D": 0,
    "3D": 0,
    "4D": 0,
    "5D": 0,
    "6D": 0,
    "MaxD": 0,
    "MinD": 0,
    "3_of_kD": 0,
    "StrD": 0,
    "F_hD": 0,
    "4_of_kD": 0,
    "JAMBD": 0
}
score1 = {
    "1U": 0,
    "2U": 0,
    "3U": 0,
    "4U": 0,
    "5U": 0,
    "6U": 0,
    "MaxU": 0,
    "MinU": 0,
    "3_of_kU": 0,
    "StrU": 0,
    "F_hU": 0,
    "4_of_kU": 0,
    "JAMBU": 0
}
score2 = {
    "1M": 0,
    "2M": 0,
    "3M": 0,
    "4M": 0,
    "5M": 0,
    "6M": 0,
    "MaxM": 0,
    "MinM": 0,
    "3_of_kM": 0,
    "StrM": 0,
    "F_hM": 0,
    "4_of_kM": 0,
    "JAMBM": 0
}
score3 = {
    "1S": 0,
    "2S": 0,
    "3S": 0,
    "4S": 0,
    "5S": 0,
    "6S": 0,
    "MaxS": 0,
    "MinS": 0,
    "3_of_kS": 0,
    "StrS": 0,
    "F_hS": 0,
    "4_of_kS": 0,
    "JAMBS": 0
}
score4 = {
    "1N": 0,
    "2N": 0,
    "3N": 0,
    "4N": 0,
    "5N": 0,
    "6N": 0,
    "MaxN": 0,
    "MinN": 0,
    "3_of_kN": 0,
    "StrN": 0,
    "F_hN": 0,
    "4_of_kN": 0,
    "JAMBN": 0
}
score5 = {
    "1R": 0,
    "2R": 0,
    "3R": 0,
    "4R": 0,
    "5R": 0,
    "6R": 0,
    "MaxR": 0,
    "MinR": 0,
    "3_of_kR": 0,
    "StrR": 0,
    "F_hR": 0,
    "4_of_kR": 0,
    "JAMBR": 0
}
scores = [score, score1, score2, score3, score4, score5]
all = 0
while True:
    for keys_values in zip(*[d.items() for d in scores]):
        for key, value in keys_values:
            print(f"{key:5}: {value}\t", end="")
        print()
    first_round.clear()
    tries = 0
    total_sum = 0
    numbers = 6
    mistake = 0
    collection.clear()
    while tries < 3:
        for number in range(numbers):
            collection.append(random.choice(dice))
        print(f"Random numbers: {collection}")

        answer = input("Do you want to keep any of the numbers(Y/N)?: ")
        if answer.lower() == "y":
            first_num = input("Which numbers do you want to keep (comma separated)?: ").split(",")
            first_num = [int(i.strip()) for i in first_num]
            print(f"You chose to keep: {first_num}")

            how_many = len(first_num)
            numbers = numbers - how_many

            for num in first_num:
                first_round.append(num)

        print(f"You have: {first_round}")
        collection.clear()
        tries += 1
    for i in first_round:
        total_sum = total_sum + i

    temporary = input("To what key do you want to add this result?: ")
    matched = False
    for score_dict in scores:
        if temporary in score_dict:
            matched = True
            if temporary == "3_of_kD" or temporary == "3_of_kU" or temporary == "3_of_kM" or temporary == "3_of_kS" or temporary == "3_of_kN" or temporary == "3_of_kR":
                # Add 20 if the value is not already set to 0
                score_dict[temporary] = total_sum
                if score_dict[temporary] != 0:
                    score_dict[temporary] += 20
            elif temporary == "StrD" or temporary == "StrU" or temporary == "StrM" or temporary == "StrS" or temporary == "StrN" or temporary == "StrR":
                score_dict[temporary] += 50
            elif temporary == "F_hD" or temporary == "F_hU" or temporary == "F_hM" or temporary == "F_hS" or temporary == "F_hN" or temporary == "F_hR":
                score_dict[temporary] = total_sum
                if score_dict[temporary] != 0:
                    score_dict[temporary] += 30
            elif temporary == "4_of_kD" or temporary == "4_of_kU" or temporary == "4_of_kM" or temporary == "4_of_kS" or temporary == "4_of_kN" or temporary == "4_of_kR":
                score_dict[temporary] = total_sum
                if score_dict[temporary] != 0:
                    score_dict[temporary] += 40
            elif temporary == "JAMBD" or temporary == "JAMBU" or temporary == "JAMBM" or temporary == "JAMBS" or temporary == "JAMBN" or temporary == "JAMBR":
                score_dict[temporary] = total_sum
                if score_dict[temporary] != 0:
                    score_dict[temporary] += 50
            else:
                score_dict[temporary] = total_sum
            break

    if not matched:
        print("Invalid input. Please try again!")

    if input("Still playing? (type 'x' for no): ") == "x":
        for keys_values in zip(*[d.items() for d in scores]):
            for key, value in keys_values:
                print(f"{key:5}: {value}\t", end="")
            print()
        break
    else:
        continue
print()
# After the main loop ends (when the player chooses to stop)
total_score = 0  # Variable to hold the sum of all scores

# Loop over all score dictionaries
for score_dict in scores:
    total_score += sum(score_dict.values())  # Add the sum of all values in the score dictionary to total_score

# Print the total score
print(f"YOUR YATZEE RESULT IS: {total_score}")