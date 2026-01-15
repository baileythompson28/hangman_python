def start_game():
    """starts the game"""
    while True:
        user_input = input("Would you like to play a game? (yes/no): ").strip().lower()
        if user_input in ['yes']:
            print("Starting the game...")
            break
        elif user_input in ['no']:
            print("Goodbye")
            break
        else:
            print("Invalid response. Enter 'yes' or 'no'.")


if __name__ == "__main__":
    start_game()