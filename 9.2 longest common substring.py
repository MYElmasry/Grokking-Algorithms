wordA = input()
wordB = input()
cell = [[0]* len(wordB) for _ in range(len(wordA))]
# print(cell)
for i in range(len(wordA)):
    for j in range(len(wordB)):
        if wordA[i] == wordB[j]:
            if i == 0:
                cell[i][j] = 1
            else:
                cell[i][j] = cell[i-1][j-1] + 1
for i in range(len(wordA)):
    print(cell[i])
    
import numpy as np
cell = np.array(cell)
maximum = np.amax(cell)

def index2D(cell, maximum):
    for i, x in enumerate(cell):
        if maximum in x:
            return i
end = index2D(cell, maximum)
print("The longest Common Substring is", wordA[end-maximum+1:end+1])