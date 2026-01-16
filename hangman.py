import random

def start_game():
    """starts the game"""
    while True:
        user_input = input("Would you like to play? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            play_again()
        elif user_input in ['no', 'n']:
            print("Goodbye")
            break
        else:
            print("Invalid response. Enter 'yes' or 'no'.")


def gameplay():
    """initial setup - contains strikes and the list of 10 words"""
    strikes = 0
    words = load_words('words.txt')
    chosen_word = random.choice(words).lower()
    guessed_letters = set()
    max_strikes = 6
    
    """Contains the game itself"""
    print("Welcome to Hangman!")
    while strikes < max_strikes:
        display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in chosen_word])
        print(f"\nWord: {display_word}")
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single character")
            continue
        if guess in guessed_letters:
            print("Already guessed that letter. Try again.")
            continue
        guessed_letters.add(guess)
        if guess not in chosen_word:
            strikes += 1
            print(f"\nWrong. Strikes: {strikes}/{max_strikes}")
        if all(letter in guessed_letters for letter in chosen_word):
            print(f"\nYou guessed the word: {chosen_word}")
            break
    else:
        print(f"\nGame over. The word was: {chosen_word}")


def load_words(filename):
    """loads words from a file and returns them as a list"""
    with open(filename, 'r') as file:
        words = [line.strip() for line in file if line.strip()]
    return words


def play_again():
    """asks the user if they want to play again"""
    gameplay()
    while True:
        replay_input = input("Would you like to play again? (yes/no): ").strip().lower()
        if replay_input in ['yes', 'y']:
            gameplay()
        elif replay_input in ['no', 'n']:
            print("Thanks for playing...")
            break
        else:
            print("Invalid response. Enter 'y' or 'n'")


if __name__ == "__main__":
    start_game()