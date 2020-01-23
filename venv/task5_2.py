def vvod_dannyh():
    f=open('data.txt','r')
    s = []
    for i in range(10):
        x = f.readline().split()
        s.append(x)
    f.close()
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
    f=open("result2.txt","w")
    print("Максимальное число:", list[0], "Минимальное: ", list[1], " Разность: ",int(list[0])-int(list[1]),file=f)
    return
vyvod_resultata(raschet(vvod_dannyh()))