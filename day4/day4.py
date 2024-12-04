from itertools import product

with open("day4/input.txt") as f:
    mat = [[c for c in row.strip()] for row in f.readlines()]

nrows = len(mat)
ncols = len(mat[0])

## P1

neighbors = list(product([1, 0, -1], [1, 0, -1]))
neighbors.remove((0, 0))  # self isn't a neighbor

TARGET = "XMAS"

tot = 0

for i0, j0 in product(range(nrows), range(ncols)):

    for di, dj in neighbors:

        failed = False

        for n in range(4):

            i = i0 + n * di
            j = j0 + n * dj

            # out of bounds -> not a match
            if i < 0 or i >= nrows or j < 0 or j >= ncols:
                failed = True
                break

            # incorrect char -> not a match
            if mat[i][j] != TARGET[n]:
                failed = True
                break

        if n == 3 and not failed:
            tot += 1

print(tot)

## P2

tot = 0
TARGET = {"M", "S"}

for i0, j0 in product(range(1, nrows - 1), range(1, ncols - 1)):

    if mat[i0][j0] == "A":

        if {mat[i0 - 1][j0 + 1], mat[i0 + 1][j0 - 1]} == TARGET:  # TL BR

            if {mat[i0 + 1][j0 + 1], mat[i0 - 1][j0 - 1]} == TARGET:  # TR BL

                tot += 1
print(tot)
