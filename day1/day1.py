with open("day1/input.txt", "r") as f:
    a, b = zip(*[[int(x) for x in y.strip().split()] for y in f.readlines()])
print(sum([abs(i - j) for i, j in zip(sorted(a), sorted(b))]))
print(sum([i * b.count(i) for i in set(a)]))
