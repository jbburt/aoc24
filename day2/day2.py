with open("day2/input.txt") as f:
    data = [[int(x) for x in y.strip().split()] for y in f.readlines()]


def gt(a, b):
    return a > b


def lt(a, b):
    return a < b


def evaluate(row):
    op = lt if row[1] > row[0] else gt
    for x, y in zip(row[:-1], row[1:]):
        if x == y or (not op(x, y)) or (abs(x - y) > 3):
            return False
    return True


safe_rows = set()
for i, row in enumerate(data):
    if evaluate(row):
        safe_rows.add(i)
print(len(safe_rows))


for i, row in enumerate(data):
    if i in safe_rows:
        continue
    for j in range(len(row)):
        pseudo_row = [z for k, z in enumerate(row) if k != j]
        if evaluate(pseudo_row):
            safe_rows.add(i)
            break
print(len(safe_rows))
