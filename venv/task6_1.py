def slovar(name_of_file):
    file = open(name_of_file, 'r')
    a = []
    b = {}

    for i in range(4):
        c = file.readline()
        d = c.split(":")
        b["first"] = int(d[0])
        b["second"] = int(d[1])
        a.append(b.copy())
    file.close()
    return a


result = slovar("slovar.txt")
print(result)