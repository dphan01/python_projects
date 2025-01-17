import random
import logging
from bs4 import BeautifulSoup
import requests

url = "https://list.fandom.com/wiki/List_of_common_animals"
page = requests.get(url, verify=False)
page_html = BeautifulSoup(page.text, "html.parser")
# print(page_html.prettify())

table = page_html.find("table", {"class": "multicol"})
animal_list = table.find_all(["a", "span"])
animals = [a.get_text(strip=True) for a in animal_list]

print("Welcome to the Hangman Game - An Animals' Version 😊\nYou'll be give the name of one animal at a time and have 7 attempts to find out what it is!\nHave fun and Good Luck 🤞")
def hangman_game():
    while True:
        logger = logging.getLogger()
        attempts = 7
        random_animal = random.choice(animals).lower()
        # print(random_animal)

        no_of_words = len(random_animal.split())

        display = ["_" for letter in random_animal]
        for index, letter in enumerate(random_animal):
            if letter == " ":
                display[index] = " "

        print(f"This animal's name contains {no_of_words} words! It looks like this: {display}")

        while attempts > 0 and "_" in display:
            guess_letter = input("Guess a letter: ").lower().strip()

            if guess_letter == "exit":
                logger.info("Exiting the game")
                print("You exited the game. Goodbye👋")
                exit(1)

            if guess_letter not in random_animal:
                attempts -= 1
                if attempts == 0:
                    print(f"Oh no you used up all your attempts, the correct word is '{random_animal}'. You lost 😔")
                else:
                    print(f"The word you must guess does not contain {guess_letter}. You have {attempts} attempts left.")
            else:
                for index, letter in enumerate(random_animal):
                    if guess_letter == letter:
                        display[index] = guess_letter

                correct_guesses = len([char for char in display if char != "_" and char != " "])
                if " " not in random_animal and correct_guesses == len(random_animal):
                    print(f"Congratulations 🎉 You have unlocked the whole word!! It is '{random_animal}'.")
                elif " " in random_animal and correct_guesses + 1 == len(random_animal):
                    print(f"Congratulations 🎉 You have unlocked the whole word!! It is '{random_animal}'.")
                else:
                    print(f"Good job! You've unlocked {correct_guesses} correct letters so far 👏 Now it looks like this: {display}")

        play_again = input("Do you want to play another round? (y/n) ").lower().strip() == "n"
        if play_again:
            print("Thanks for playing, goodbye👋")
            break


hangman_game()