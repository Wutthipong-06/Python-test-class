weights = []

while True:
    w = int(input())
    if w == 0:
        break
    weights.append(w)

command = input().strip().lower()

if command == "max":
    weights.sort(reverse=True) 
elif command == "min":
    weights.sort()             
else:
    print()
    exit()
for w in weights:
  print(w, end=" ")
