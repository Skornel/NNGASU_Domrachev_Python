def slovar():
    file = open('slovar.txt', 'r')
    a = []
    b = {}

    for i in range(4):
        c = file.readline()
        d = c.split(":")
        b["first"] = d[0]
        b["second"] = d[1]
        a.append(b.copy())
    file.close()
    return a


def func_2(array, string):
    result = []
    for i in array:
        if string == i['first'] or string == i['second']:
            result.append(i)
    return result


result = slovar()
print(result)
string = input("Введите строку: ")
res2 = func_2(result, string)
if res2:
    print(res2)
else:
    print(result)