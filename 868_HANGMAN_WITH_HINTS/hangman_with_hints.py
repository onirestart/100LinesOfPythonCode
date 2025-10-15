import random


WORDS_WITH_HINTS = [
    ('python', 'A popular programming language'),
    ('computer', 'An electronic device for processing data'),
    ('keyboard', 'Input device with keys'),
    ('internet', 'Global network of computers'),
    ('algorithm', 'Step-by-step problem-solving procedure'),
    ('database', 'Organized collection of data'),
    ('software', 'Programs and applications'),
    ('hardware', 'Physical computer components'),
]

HANGMAN_STAGES = [
    '  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========',
    '  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========',
    '  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========',
    '  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========',
    '  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========',
    '  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========',
    '  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========',
]


def display_game_state(word, guessed_letters, wrong_attempts):
    """Display current game state."""
    print('\n' + HANGMAN_STAGES[wrong_attempts])
    display = ' '.join(c if c in guessed_letters else '_' for c in word)
    print(f'\nWord: {display}')
    print(f'Guessed: {", ".join(sorted(guessed_letters))}')
    print(f'Attempts left: {6 - wrong_attempts}')


def play_game():
    """Main game logic."""
    word, hint = random.choice(WORDS_WITH_HINTS)
    guessed_letters = set()
    wrong_attempts = 0
    hint_used = False
    max_attempts = 6

    print('\nWelcome to Hangman with Hints!')
    print(f'Word has {len(word)} letters')

    while wrong_attempts < max_attempts:
        display_game_state(word, guessed_letters, wrong_attempts)

        if set(word) <= guessed_letters:
            print(f'\n🎉 Congratulations! You won! The word was: {word}')
            return

        guess = input('\nGuess a letter (or "hint" for help): ').lower()

        if guess == 'hint':
            if not hint_used:
                print(f'Hint: {hint}')
                hint_used = True
            else:
                print('Hint already used!')
            continue

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue

        if guess in guessed_letters:
            print('You already guessed that letter!')
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f'✓ Correct! "{guess}" is in the word!')
        else:
            wrong_attempts += 1
            print(f'✗ Wrong! "{guess}" is not in the word.')

    display_game_state(word, guessed_letters, wrong_attempts)
    print(f'\n💀 Game Over! The word was: {word}')


if __name__ == '__main__':
    play_game()
