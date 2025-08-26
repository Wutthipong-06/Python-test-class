num = 1101700203451
num_12 = int(str(num)[:-1])
di = [int(d) for d in str(num_12)]
start = len(di) + 2

re = []
for i, d in enumerate(di):
  w = start - i
  re.append(d * w)
  print(sum(re))