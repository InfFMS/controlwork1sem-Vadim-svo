def F(a, b):
    if a > b:
        if F(a, b) == F(a-1, b):
            return(1)
    else:
        if F(a, b) == F(a, b-1):
            return(1)

F = 0
a = 0
b = 0
while F != 1:
    a += 1
    b += 1
    F(a, b)