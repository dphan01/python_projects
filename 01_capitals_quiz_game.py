import requests
import random

url = 'https://countriesnow.space/api/v0.1/countries/capital'

response = requests.get(url, verify=False).json()

data = response["data"]
def capital_quiz():
    iteration = 0
    score = 0
    no_of_questions = 0

    while True:
        game_level = input("Difficulty level (Easy, Medium or Hard)? : \n").lower()

        if game_level not in ["easy", "medium", "hard"]:
            print("That's not a correct answer, perhaps you made a typo. Choose again. ")
        else:
            if game_level == "easy":
                no_of_questions += 5
            elif game_level == "medium":
                no_of_questions += 10
            elif game_level == "hard":
                no_of_questions += 20
            print(f"There will be {no_of_questions} questions. Let's start and Good luck!:')")
            break

    while iteration < no_of_questions:
        random_pick = random.choice(data)
        answer = input(f"What's the capital of {random_pick["name"]}?\n").strip().lower()
        if answer == random_pick["capital"].lower():
            score += 1
            print("That's correct! One score for you:) ")
        elif game_level == "exit":
            print("You're exiting the game. Goodbye!")
            exit(1)
        else:
            print(f"That's not correct. The capital of {random_pick["name"]} is {random_pick["capital"]}.")
        iteration += 1

    correct_percentage = round(score / no_of_questions * 100, 0)

    if correct_percentage <= 39:
        print(f"You're a Beginner Explorer with {score} correct answers 🌍 Keep learning and exploring the world!")
    elif correct_percentage <= 79:
        print(f"You're a Seasoned Traveler with {score} correct answers ✈️ Great job! You know your way around many capitals.")
    else:
        print(f"You're a Capital Master with {score} correct answers🏆 Outstanding! You're a true expert in world capitals.")


capital_quiz()