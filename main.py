def calculate_points(gry):
    total = 0
    for i in range(10):
        for j in range(10):
            if gry[i][j] == 'X':
                total += min(i + 1, j + 1, 10 - i, 10 - j)#yoo its rewind time
    return total


t = int(input())
for _ in range(t):
    grid = [input() for _ in range(10)]
    total_points = calculate_points(grid)
    print(total_points)
