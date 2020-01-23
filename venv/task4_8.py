def output(str1,str2,number):
    str2[:number]+str1+str2[number:]
    return str2[:number] + str1 + str2[number:]
str1=input("Введите первую строку: ")
str2=input("Введите вторую строку: ")
number=input("Введите номер: ")
print(output(str1, str2, int(number)))
