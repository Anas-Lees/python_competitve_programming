#A. Beautiful Matrix
matrix = []
for i in range(5):
    a = list(map(int, input().split()))
    matrix.append(a)
b = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            print(abs(2 - i) + abs(2 - j))
#https://codeforces.com/problemset/problem/263/A