a = int(input())
b = int(input())
c = int(input())
d = int(input())
C = a*1000 + b*100 + c*10 + d
a1 = a + b
a2 = b+c
a3 = c+d

F = []
F.append(a1)
F.append(a2)
F.append(a3)
print(F)
F.sort()
print(F)

Gt = F[1]*100 + F[2]
print(Gt)

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                a = i
                b = j
                c = k
                d = l
                C = a * 1000 + b * 100 + c * 10 + d
                a1 = a + b
                a2 = b + c
                a3 = c + d
                F = []
                F.append(a1)
                F.append(a2)
                F.append(a3)
                print(F)
                F.sort()
                print(F)
                print('ААА', a, b, c, d)
                Gt = F[1] * 100 + F[2]
                print(Gt)
                if Gt == 1418:
                    break
                    print('ААА', a, b, c, d)

#Ответ 1599