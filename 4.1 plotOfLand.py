def divide(x, y):
    if x == y:
        return x
    if x > y:
        return divide(x-y, y)
    if x < y:
        return divide(x, y-x)
        
print(divide(64, 40))