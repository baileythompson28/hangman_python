def start_game():
    while True:
        user_input = input("Would you like to play a game? (yes/no): ").strip().lower()
        if user_input in ['yes']:
            print("Starting the game...")
            # Here you would add the code to start the actual game
            break
        elif user_input in ['no']:
            print("Goodbye")
            break
        else:
            print("Invalid response. Enter 'yes' or 'no'.")


if __name__ == "__main__":
    start_game()