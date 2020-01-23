first=input("Введите первое число: ")
second=input("Введите второе число: ")
thrith=input("Введите третье число: ")
if (first>second and first>thrith):
    print("Наибольшее число", first)
else:
    if (second>first and second>thrith):
        print("Наибольшее число: ", second)
    else:
        print("Наибольшее число: ", thrith)