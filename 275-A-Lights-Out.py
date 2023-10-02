grid = []
for _ in range(3):
    row = list(map(int, input().split()))
    grid.append(row)
current_state = [[1] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        sum = grid[i][j]
        if i > 0:
            sum += grid[i - 1][j]
        if i < 2:
            sum += grid[i + 1][j]
        if j > 0:
            sum += grid[i][j - 1]
        if j < 2:
            sum += grid[i][j + 1]
        if sum % 2 == 1:
            current_state[i][j] = 0
for row in current_state:
    print("".join(map(str, row)))


#https://codeforces.com/problemset/problem/275/A