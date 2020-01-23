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
    for i in range(4):
        if int(list[i][0]) > int(maximum):
            maximum = list[i][0]
    print(maximum)
    for i in range(4):
        if int(list[i][0]) == int(maximum):
            b = list[i]
            list[i] = list[0]
            list[0] = b
    return list
def vyvod_resultata(list):
    print(list)
    return
vyvod_resultata(raschet(vvod_dannyh()))
