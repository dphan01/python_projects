import random
import pandas as pd


sheet_name = "my_czech_english_dictionary"
sheet_id = "1jyQ2x6d00ejAAeHqdUiOLt8SlWI6erwseYe3xnuzLqo"

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)
# print(df)

def flashcards_generator():
    cont = True
    while cont:
        random_word = random.choice(df["Czech"])
        print(f"Your random word is '{random_word}'")

        want_answer = input("Do you want to know what it means? (y/n) ").lower() == "y"

        meaning = df[df["Czech"] == random_word]["English"].item()
        if want_answer:
            print(f"'{random_word}' means '{meaning}'.")

        question = input("Do you want another word? (y/n) ").lower()
        if question == "n":
            break

flashcards_generator()