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
minimum=1000
for i in range(len(s)):
    for j in range(len(s[i])):
        if int(s[i][j])>int(maximum):
            maximum=s[i][j]
        if int(s[i][j])<int(minimum):
            minimum=s[i][j]
print("Максимальное число:", maximum, "Минимальное: ", minimum, " Разность: ",int(maximum)-int(minimum))