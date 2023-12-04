
def make_grid(input):
    with open('data/3.txt') as f:
        lines = f.readlines()
        return lines

def find_next_number(startY, startX, grid):
    y, x = [startY, startX]
    value = 0
    while x < len(grid[y]) and value == 0:
        if grid[y][x].isdigit():
            while x+1 < len(grid[y]) and grid[y][x].isdigit():
                value = value*10 + int(grid[y][x])
                x += 1
        x += 1
    return x, value

def not_number_or_dot(string):
    for char in string:
        return not (char.isdigit() or char == '.')

def has_adjacent_symbol(startX, endX, Y, grid):
    if Y > 0 and startX > 0 and endX < len(grid[Y])-1 and Y < len(grid)-1:
        if (
                not_number_or_dot(grid[Y-1][startX-1:endX+1]) or
                not_number_or_dot(grid[Y][startX-1]) or
                not_number_or_dot(grid[Y][endX+1]) or
                not_number_or_dot(grid[Y+1][startX-1:endX+1])
            ):
            return True
    if Y == 0 and startX > 0 and endX < len(grid[Y])-1 and Y < len(grid)-1:
        if (
                not_number_or_dot(grid[Y][startX-1]) or
                not_number_or_dot(grid[Y][endX+1]) or
                not_number_or_dot(grid[Y+1][startX-1:endX+1])
            ):
            return True
    if Y > 0 and startX > 0 and endX < len(grid[Y])-1 and Y >= len(grid)-1:
        if (
                not_number_or_dot(grid[Y-1][startX-1:endX+1]) or
                not_number_or_dot(grid[Y][startX-1]) or
                not_number_or_dot(grid[Y][endX+1])
            ):
            return True
    if Y > 0 and startX <= 0 and endX < len(grid[Y])-1 and Y < len(grid)-1:
        if (
                not_number_or_dot(grid[Y-1][startX-1:endX+1]) or
                not_number_or_dot(grid[Y][endX+1]) or
                not_number_or_dot(grid[Y+1][startX-1:endX+1])
            ):
            return True        
    if Y > 0 and startX > 0 and endX >= len(grid[Y])-1 and Y < len(grid)-1:
        if (
                not_number_or_dot(grid[Y-1][startX-1:endX+1]) or
                not_number_or_dot(grid[Y][startX-1]) or
                not_number_or_dot(grid[Y+1][startX-1:endX+1])
            ):
            return True

def sum_part_numbers(grid):
    sum = 0
    currentY, currentX = [0, 0]
    for currentY in range(len(grid)):
        for currentX in range(len(grid[currentY])):
            currentX, value = find_next_number(currentY, currentX, grid)

            if has_adjacent_symbol(currentX-len(str(value))+1, currentX, currentY, grid):
                sum += value
    return sum

grid = make_grid(input)
print(sum_part_numbers(grid))

