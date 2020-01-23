def slovar():
    h_file = open('slovar.txt', 'r')
    a = []
    b = {}

    for i in range(4):
        c = h_file.readline()
        d = c.split(":")
        b["first"] = d[0]
        b["second"] = d[1]
        a.append(b.copy())

    return a


def slovar2(res):
    s = {}
    s['first'] = input()
    s['second'] = input()

    res.append(s.copy())

    return res


def vyvod(sl):
    f = open('slovar2.txt', 'w')
    for x in sl:
        print(x['first'] + " \t " + x['second'], file=f)


res = slovar()
print(res)
sl = slovar2(res)
print(sl)
vyvod(sl)
#Git test