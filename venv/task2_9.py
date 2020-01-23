#Это 2_13. А 2_9 в 2_13
s=[]
for i in range(4):
    b=[]
    print("Введите данные ",i+1," списка")
    for row in range(4):
        print("Вводи ",row+1," элемент ",i+1," списка ")
        b.append(input())
    s.append(b)
print(s)
maximum=0
for i in range(4):
    if int(s[i][0])>int(maximum):
        maximum=s[i][0]
print(maximum)
for i in range(4):
    if int(s[i][0])==int(maximum):
        b=s[i]
        s[i]=s[0]
        s[0]=b
print(s)