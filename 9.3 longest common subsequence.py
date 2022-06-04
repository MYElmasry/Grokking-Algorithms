wordA = input()
wordB = input()

rows, cols = (len(wordA), len(wordB))

cell = [[0]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if wordA[i] == wordB[j]:
            
            cell[i][j] = cell[i-1][j-1]+1
        else:
            cell[i][j] = max(cell[i][j-1], cell[i-1][j])

import numpy as np
cell = np.array(cell)
maximum = np.amax(cell)
print(maximum)