#!/usr/bin/env python


def cinput(prompt: str | None = None) -> str:
    if prompt:
        print(prompt)
    return input().strip().lower()


def ask_yes(question: str) -> bool:
    return cinput(question) == "yes"


def ask_character(name: str) -> None:
    if ask_yes(f"Is your character {name}?"):
        print("Guessed right another time :)")
    else:
        print("That's embarrassing, let's try again.")


def main() -> None:
    # Friend Guesser
    print("Welcome, I'm AkinatorGuyyy!")
    print("Today I will manage to guess your friend! (As long as cycy added them!)")
    print("Please answer the following questions with 'yes' or 'no'\n")

    # Questions
    if ask_yes("Is your character a male?"):
        if ask_yes("Do they like math?"):
            ask_character("Cycy")
        else:
            ask_character("Bareth")
    else:
        ask_character("SOMEONE")


if __name__ == "__main__":
    main()
