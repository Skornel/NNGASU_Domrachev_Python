#Возьмём за базу 4_17, добавим булево значение - ??? - PROFIT
def vvod():
    return input("Введите строку: ")
def answer(string):
    Here=False
    if(string.count(input("Введите необходимое слово для поиска: "))):
        Here=True
    return Here
print(answer(vvod()))