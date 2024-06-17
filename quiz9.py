import random

def generate_maze(N, M):
    # 生成一個 NxM 的初始迷宮，每個單元格的初始值為0（空白）
    return {(i, j): 0 for i in range(N) for j in range(M)}

def add_obstacles(maze, min_obstacles, N, M):
    # 在迷宮中隨機添加障礙物
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze[(i, j)] == 0]
    max_obstacles = len(empty_cells)
    if min_obstacles > max_obstacles:
        min_obstacles = max_obstacles
        print(f"Maximum obstacles set to {max_obstacles} due to limited empty cells.")
    
    for _ in range(min_obstacles):
        if not empty_cells:
            break
        cell = random.choice(empty_cells)
        maze[cell] = 1
        empty_cells.remove(cell)
    return maze

def set_obstacle(maze, N, M):
    # 設置障礙物
    try:
        x, y = map(int, input("Enter coordinates to set obstacle (row col): ").split())
        if (x, y) in maze and maze[(x, y)] == 0:
            maze[(x, y)] = 1
        else:
            print("Invalid coordinates or cell is not empty.")
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
    return maze

def remove_obstacle(maze, N, M):
    # 移除障礙物
    try:
        x, y = map(int, input("Enter coordinates to remove obstacle (row col): ").split())
        if (x, y) in maze and maze[(x, y)] == 1:
            maze[(x, y)] = 0
        else:
            print("Invalid coordinates or cell is not an obstacle.")
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
    return maze

def print_maze_from_grid(grid):
    # 打印從文件讀取的原始迷宮
    for line in grid:
        print(line)

def print_maze(maze, N, M):
    # 打印當前迷宮狀態
    for i in range(N):
        print("+---" * M + "+")
        for j in range(M):
            if maze[(i, j)] == 0:
                print("|   ", end="")
            elif maze[(i, j)] == 1:
                print("| X ", end="")
            elif maze[(i, j)] == 2:
                print("| O ", end="")
        print("|")
    print("+---" * M + "+")

def generate_path(maze, N, M):
    # 生成從左上角到右下角的路徑
    path = []
    x, y = 0, 0
    while x < N and y < M:
        maze[(x, y)] = 2
        path.append((x, y))
        if x == N-1 and y == M-1:
            break
        if x < N-1 and y < M-1:
            if random.choice([True, False]):
                x += 1
            else:
                y += 1
        elif x < N-1:
            x += 1
        else:
            y += 1
    return maze, path

def main():
    # 主函數
    while True:
        filename = input("Enter the filename: ")
        try:
            with open(filename, 'r') as file:
                grid = [line.strip() for line in file.readlines()]
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
    
    print("Original grid from file:")
    print_maze_from_grid(grid)
    
    N = len(grid)
    M = (len(grid[0]) + 1) // 4  # 考慮到網格格式包含'|'和空格

    maze = {(i, j): 1 if grid[i][j*4+1] == 'X' else 0 for i in range(N) for j in range(M)}

    maze, path = generate_path(maze, N, M)
    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
            if min_obstacles < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid number of obstacles. Please enter a non-negative integer.")
    
    maze = add_obstacles(maze, min_obstacles, N, M)
    print("Maze with added obstacles:")
    print_maze(maze, N, M)

    while True:
        option = input("Choose an option: (S)et obstacle, (R)emove obstacle, (E)xit: ").strip().upper()
        if option == 'S':
            maze = set_obstacle(maze, N, M)
        elif option == 'R':
            maze = remove_obstacle(maze, N, M)
        elif option == 'E':
            break
        else:
            print("Invalid option.")
        print("Current maze state:")
        print_maze(maze, N, M)

if __name__ == "__main__":
    main()
