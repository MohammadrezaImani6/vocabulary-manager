import json
import random

try:
    with open("data.json", "r", encoding="utf_8") as f:
        words = json.load(f)
except FileNotFoundError:
    words = {}


def file(words):
    with open("data.json", "w", encoding="utf_8") as f:
        json.dump(words, f, ensure_ascii=False, indent=4)
    with open("words.txt", "w", encoding="utf_8") as f:
        for word, info in words.items():
            f.write(f"Word: {word}\n")
            f.write(f"Meaning: {info['meaning']}\n")
            f.write(f"Example: {info['example']}\n")
            f.write("-----------------------------------\n")


def add_word(words):
    word = input("Enter new word: ").lower().title()
    if not word.isalpha():
        print("❌Invalid input.")
        return
    if word in words:
        print("Word already exsits.")
        return
    meaning = input("The meaning: ")
    example = input("Example: ").title()
    words[word] = {"meaning": meaning, "example": example}
    print(f'"{word}" added✅')
    file(words)


def search_word(words):
    user_search = input("Enter the word you want to find: ").lower().title()
    if user_search in words:
        print(f"Meaning:{words[user_search]['meaning']}")
        print(f"Example:{words[user_search]['example']}")
    else:
        print("The word not found.")


def edit_word(words):
    user_edit = input("Enter the word to edit it: ").lower().title()
    if user_edit in words:
        meaning_edit = input("The meaning: ")
        example_edit = input("Example: ").title()
        words[user_edit]["meaning"] = meaning_edit
        words[user_edit]["example"] = example_edit
        print(f"{user_edit} updated✅")
        file(words)
    else:
        print("The word not found.")


def delete_word(words):
    user_delete = input("Enter the word to remove it: ").lower().title()
    if user_delete in words:
        del words[user_delete]
        print(f"{user_delete} deleted✅")
        file(words)
    else:
        print("The word not found.")


def show_all_words(words):
    if not words:
        print("No words available.")
        return
    for word, info in sorted(words.items()):
        print(f"Word:{word}")
        print(f"Meaning:{info['meaning']}")
        print(f"Example:{info['example']}")


def quiz(words):
    if not words:
        print("No words available.")
        return
    x = random.choice(list(words.keys()))
    print(f"The meaning is: {words[x]['meaning']}")
    user_guess = input("Guess the word: ").lower().title()
    if user_guess == x:
        print("Nice you guess correct✅")
    else:
        print(f"Ohh incorrect answer.\n Correct answer:{x}")


def statistics(words):
    count = len(words)
    print(f"Total words= {count}")


while True:
    print(
        "1) Add word\t2) Search word\t3) Edit word\n4) Delete word\t5) Show all words\t6) Quiz\n7) Statistics\t8) Exit"
    )
    try:
        user = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input.")
        continue
    if user == 1:
        add_word(words)
    elif user == 2:
        search_word(words)
    elif user == 3:
        edit_word(words)
    elif user == 4:
        delete_word(words)
    elif user == 5:
        show_all_words(words)
    elif user == 6:
        quiz(words)
    elif user == 7:
        statistics(words)
    elif user == 8:
        break
