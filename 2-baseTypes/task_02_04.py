a, b = map(int, input().split())
while a != 0: a, b = abs(b - a), a
print(b)