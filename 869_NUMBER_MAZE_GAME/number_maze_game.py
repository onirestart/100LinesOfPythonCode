import random
import os
import sys


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_maze(size=8):
    """Create a random number maze."""
    maze = [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]
    start = (0, 0)
    goal = (size - 1, size - 1)
    maze[start[0]][start[1]] = 'S'
    maze[goal[0]][goal[1]] = 'G'
    return maze, start, goal


def display_maze(maze, player_pos):
    """Display the maze with player position."""
    clear_screen()
    print("\nNumber Maze Game - Reach the Goal (G)!\n")
    print("Controls: W=Up, A=Left, S=Down, D=Right, Q=Quit\n")
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                print('[P]', end=' ')
            elif cell == 'S':
                print('[S]', end=' ')
            elif cell == 'G':
                print('[G]', end=' ')
            else:
                print(f'[{cell}]', end=' ')
        print()
    print()


def get_move():
    """Get player move input."""
    if os.name == 'nt':
        import msvcrt
        key = msvcrt.getch().decode('utf-8').upper()
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1).upper()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key


def move_player(pos, direction, size):
    """Calculate new player position."""
    y, x = pos
    if direction == 'W' and y > 0:
        return (y - 1, x)
    elif direction == 'S' and y < size - 1:
        return (y + 1, x)
    elif direction == 'A' and x > 0:
        return (y, x - 1)
    elif direction == 'D' and x < size - 1:
        return (y, x + 1)
    return pos


def play_game():
    """Main game logic."""
    maze, start, goal = create_maze()
    player_pos = start
    moves = 0

    while player_pos != goal:
        display_maze(maze, player_pos)
        print(f"Moves: {moves}")
        move = get_move()

        if move == 'Q':
            print("\nGame quit. Thanks for playing!")
            return

        new_pos = move_player(player_pos, move, len(maze))
        if new_pos != player_pos:
            moves += 1
            player_pos = new_pos

    display_maze(maze, player_pos)
    print(f"\nCongratulations! You reached the goal in {moves} moves!")


if __name__ == "__main__":
    play_game()
