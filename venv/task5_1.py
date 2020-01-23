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
    f=open('result.txt','w')
    print(list, file = f)
    f.close()
vyvod_resultata(raschet(vvod_dannyh()))
