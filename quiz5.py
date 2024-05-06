n = int(input('Enter the size if the grid : '))
grid = []
for number in range(0, n**2):
    grid.append('_')

grid_str = ''
for i in range(0, n):
    row = (grid[i : i+n])
    grid_str += ' '.join(row) + '\n'
print(grid_str)

e = 0
while e != 'done':
    e = input('Enter the cell cordinates to edit : ')
    if e == 'done':
        break
    new = input('Enter the new value for the cell : ')
    edit = e.split(',')

    nte = int(edit[0])*n + int(edit[1])
    grid[nte] = new
    grid_str = ''
    for i in range(0, n*n, n):
        row = (grid[i : i+n])
        grid_str += ' '.join(row) + '\n'
    print(grid_str)
