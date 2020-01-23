def vvod_dannyh():
    s = []
    for i in range(4):
        b = []
        print("Введите данные ", i + 1, " списка")
        for row in range(4):
            print("Вводи ", row + 1, " элемент ", i + 1, " списка ")
            b.append(input())
        s.append(b)
    return s
def raschet(list):
    maximum = 0
    minimum = 1000
    for i in range(len(list)):
        for j in range(len(list[i])):
            if int(list[i][j]) > int(maximum):
                maximum = list[i][j]
            if int(list[i][j]) < int(minimum):
                minimum = list[i][j]
    #return maximum, minimum
    return [maximum,minimum]
def vyvod_resultata(list):
    print("Максимальное число:", list[0], "Минимальное: ", list[1], " Разность: ",int(list[0])-int(list[1]))
    return
vyvod_resultata(raschet(vvod_dannyh()))