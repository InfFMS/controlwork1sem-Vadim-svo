a = 125**5+25**9-30
S = 0
while a > 5:
    b = a // 5
    c = a-b*5
    if c == 4:
        S += 1
    a = b
    print (a)
    print (b)
    print (c)
    print ()

print (S)