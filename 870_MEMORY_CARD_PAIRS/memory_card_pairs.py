import random
import os


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_board(pairs=8):
    """Create a board with matching pairs."""
    symbols = list(range(1, pairs + 1)) * 2
    random.shuffle(symbols)
    return symbols, [False] * len(symbols)


def display_board(symbols, revealed, selected):
    """Display the current board state."""
    clear_screen()
    print("\nMemory Card Pairs - Match all pairs!\n")
    for i in range(len(symbols)):
        if revealed[i] or i in selected:
            print(f"[{symbols[i]:2}]", end=" ")
        else:
            print(f"[{i:2}]", end=" ")
        if (i + 1) % 4 == 0:
            print()
    print()


def get_input(prompt, max_val):
    """Get valid input from user."""
    while True:
        try:
            val = int(input(prompt))
            if 0 <= val < max_val:
                return val
            print(f"Enter a number between 0 and {max_val - 1}")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    """Main game logic."""
    symbols, revealed = create_board()
    attempts = 0
    matches = 0

    while matches < len(symbols) // 2:
        display_board(symbols, revealed, [])
        print(f"Attempts: {attempts} | Matches: {matches}/{len(symbols) // 2}")

        first = get_input("Select first card: ", len(symbols))
        while revealed[first]:
            print("Card already matched! Choose another.")
            first = get_input("Select first card: ", len(symbols))

        display_board(symbols, revealed, [first])

        second = get_input("Select second card: ", len(symbols))
        while second == first or revealed[second]:
            if second == first:
                print("Choose a different card!")
            else:
                print("Card already matched! Choose another.")
            second = get_input("Select second card: ", len(symbols))

        display_board(symbols, revealed, [first, second])
        attempts += 1

        if symbols[first] == symbols[second]:
            print("\nMatch found! ✓")
            revealed[first] = revealed[second] = True
            matches += 1
        else:
            print("\nNo match. Try again.")

        input("Press Enter to continue...")

    display_board(symbols, revealed, [])
    print(f"\nCongratulations! You won in {attempts} attempts!")


if __name__ == "__main__":
    play_game()
