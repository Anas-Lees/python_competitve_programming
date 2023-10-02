lis = []
lis.append(2)
counter = 2
for i in range(2, 51):
    counter = 2
    for j in range(2, i):
        num = i / j
        ans = i // j
        if num != ans:
            counter += 1
            if counter == i:
                lis.append(i)

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
aa = 0
bb = 0
a, b = map(int, input().split())
for i in range(15):
    if a == prime[i]:
        aa = i
    if b == prime[i]:
        bb = i
if aa == bb - 1:
    print('YES')
else:
    print('NO')

#https://codeforces.com/problemset/problem/80/A