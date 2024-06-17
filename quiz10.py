import curses
import random

# Initialize the screen
screen = curses.initscr()
curses.curs_set(0)
sh, sw = screen.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initial snake and food settings
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

food = [sh // 2, sw // 2]
w.addch(food[0], food[1], 'π')

special_food = [sh // 3, sw // 3]
w.addch(special_food[0], special_food[1], 'X')

# Generate obstacles
obstacles = []
for _ in range(int(sh * sw * 0.05 / 5)):
    if random.choice([True, False]):
        # horizontal obstacle
        start_x = random.randint(1, sw - 6)
        start_y = random.randint(1, sh - 1)
        for i in range(5):
            obstacles.append([start_y, start_x + i])
            w.addch(start_y, start_x + i, curses.A_REVERSE)
    else:
        # vertical obstacle
        start_x = random.randint(1, sw - 1)
        start_y = random.randint(1, sh - 6)
        for i in range(5):
            obstacles.append([start_y + i, start_x])
            w.addch(start_y + i, start_x, curses.A_REVERSE)

# Initialize variables
key = curses.KEY_RIGHT
normal_food_count = 0
special_food_count = 0
paused = False

def check_collision(new_head):
    """Check if the snake collides with itself or obstacles."""
    if new_head in snake or new_head in obstacles:
        return True
    return False

def generate_food(symbol):
    """Generate food at a random position not occupied by the snake or obstacles."""
    while True:
        nf = [random.randint(1, sh - 1), random.randint(1, sw - 1)]
        if nf not in snake and nf not in obstacles:
            w.addch(nf[0], nf[1], symbol)
            return nf

# Main game loop
while True:
    next_key = w.getch()
    if next_key == ord(' '):
        paused = not paused
    if not paused:
        key = key if next_key == -1 else next_key

    if paused:
        continue

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Allow the snake to wrap around the screen
    new_head[0] %= sh
    new_head[1] %= sw

    # Check for collisions
    if check_collision(new_head):
        break

    # Insert new head of the snake
    snake.insert(0, new_head)

    if new_head == food:
        normal_food_count += 1
        food = generate_food('π')
    elif new_head == special_food:
        special_food_count += 1
        special_food = generate_food('X')
        if len(snake) > 1:
            snake.pop()
    else:
        snake.pop()

    # Clear the screen and redraw everything
    w.clear()
    w.addch(food[0], food[1], 'π')
    w.addch(special_food[0], special_food[1], 'X')
    for obstacle in obstacles:
        w.addch(obstacle[0], obstacle[1], curses.A_REVERSE)
    for segment in snake:
        w.addch(segment[0], segment[1], '#')

# End the game and print the result
curses.endwin()
print(f"Game Over! Normal food eaten: {normal_food_count}, Special food eaten: {special_food_count}")
