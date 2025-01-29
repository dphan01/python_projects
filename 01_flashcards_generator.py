import random
import pandas as pd

sheet_name = "my_czech_english_dictionary"
sheet_id = "1jyQ2x6d00ejAAeHqdUiOLt8SlWI6erwseYe3xnuzLqo"

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)
# print(df)

def cz_to_en_generator():
    while True:
        random_word = random.choice(df["Czech"])
        print(f"Your random word is '{random_word}'")

        want_answer = input("Do you want to know what that means in English? (y/n) ").lower() == "y"

        meaning = df[df["Czech"] == random_word]["English"].item()
        if want_answer:
            print(f"'{random_word}' means '{meaning}'.")

        question = input("Do you want another word? (y/n) ").lower()
        if question == "n":
            break

def en_to_cz_generator():
    while True:
        random_word = random.choice(df["English"])
        print(f"Your random word is '{random_word}'")

        want_answer = input("Do you want to know how to say that in Czech? (y/n) ").lower() == "y"

        meaning = df[df["English"] == random_word]["Czech"].item()
        if want_answer:
            print(f"'{random_word}' means '{meaning}'.")

        question = input("Do you want another word? (y/n) ").lower()
        if question == "n":
            break

print("Please choose either of the following versions to start the flashcards.")
while True:
    try:
        flashcards_opt = int(input("Enter 1 for English to Czech. Enter 2 for Czech to English. Enter 3 to exit the program: "))
        if flashcards_opt == 1:
            en_to_cz_generator()
        elif flashcards_opt == 2:
            cz_to_en_generator()
        elif flashcards_opt == 3:
            print("You have exited the flashcard program...")
            exit(1)
    except ValueError:
        print("Please enter the number correctly.")
