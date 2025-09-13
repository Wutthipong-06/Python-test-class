n = int(input().strip())
data = list(map(int, input().split()))
target = int(input().strip())
if target in data:
    print("Yes")
else:
    print("No")