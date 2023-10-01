n, s = map(int, input().split())
a = [i for i in input()]
skip = False
while s > 0:
    for i in range(len(a)):
        if skip:
            skip = False
            continue
        if a[i] == 'G' and a[i - 1] == 'B' and i != 0:
            a[i], a[i - 1] = a[i - 1], a[i]
            skip = True
    s += - 1
print(''.join(a))

#https://codeforces.com/problemset/problem/266/B