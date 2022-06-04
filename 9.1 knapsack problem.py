items = {}
items["Guitar"] = (1500, 1)
items["Stereo"] = (3000, 4)
items["Laptop"] = (2000, 3)
items["Iphone"] = (2000, 1)
capacity = 4
rows, cols = (len(items), capacity)
cell = [[0]*cols for _ in range(rows)]
# print(list(items.values())[0][1])
for i in  range(list(items.values())[0][1]-1, cols):
    cell[0][i] = list(items.values())[0][0]
# print(cell)
for i in range(1, rows):
    for j in range(cols):
        if list(items.values())[i][1]-1 > j:
            cell[i][j] = cell[i-1][j]
        elif list(items.values())[i][1]-1 == j:
            cell[i][j] = list(items.values())[i][0]
        else:
            cell[i][j] = max(cell[i-1][j], cell[i-1][j-list(items.values())[i][1]]+list(items.values())[i][0])
for i in range(rows):
    print(cell[i])
    
print("The Maximum Value =", cell[rows-1][cols-1])