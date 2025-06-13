# Remove unnecessary 'all = 0'
import random
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
# Improved input validation and error handling
while True:
    first_round.clear()
    tries = 0
    total_sum = 0
    numbers = 6
    collection.clear()

    while tries < 3:
        # Roll the dice
        for number in range(numbers):
            collection.append(random.choice(dice))
        print(f"Random numbers: {collection}")

        answer = input("Do you want to keep any of the numbers(Y/N)?: ")
        if answer.lower() == "y":
            first_num = input("Which numbers do you want to keep (comma separated)?: ").split(",")
            try:
                first_num = [int(i.strip()) for i in first_num]
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue  # Ask the user again for valid input
            print(f"You chose to keep: {first_num}")

            how_many = len(first_num)
            numbers = numbers - how_many

            for num in first_num:
                first_round.append(num)

        print(f"You have: {first_round}")
        collection.clear()
        tries += 1

    # Calculate the sum of the kept dice
    total_sum = sum(first_round)

    # Ask for a key and match it
    temporary = input("To what key do you want to add this result?: ")
    matched = False
    for score_dict in scores:
        if temporary in score_dict:
            matched = True
            # Simplify the if-else structure
            key_actions = {
                "3_of_kD": 20, "3_of_kU": 20, "3_of_kM": 20, "3_of_kS": 20, "3_of_kN": 20, "3_of_kR": 20,
                "StrD": 50, "StrU": 50, "StrM": 50, "StrS": 50, "StrN": 50, "StrR": 50,
                "F_hD": 30, "F_hU": 30, "F_hM": 30, "F_hS": 30, "F_hN": 30, "F_hR": 30,
                "4_of_kD": 40, "4_of_kU": 40, "4_of_kM": 40, "4_of_kS": 40, "4_of_kN": 40, "4_of_kR": 40,
                "JAMBD": 50, "JAMBU": 50, "JAMBM": 50, "JAMBS": 50, "JAMBN": 50, "JAMBR": 50,
            }
            if temporary in key_actions:
                score_dict[temporary] = total_sum + key_actions.get(temporary, 0)
            else:
                score_dict[temporary] = total_sum
            break

    if not matched:
        print("Invalid input. Please try again!")

    # Prompt to continue or end the game
    if input("Still playing? (type 'x' for no): ") == "x":
        total_score = 0
        for score_dict in scores:
            total_score += sum(score_dict.values())
        print(f"YOUR YATZEE RESULT IS: {total_score}")
        break
    else:
        continue
