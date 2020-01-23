number=int(input("Введите трёхзначное число: "))
if (number%10==number//100):
    print("Палиндром")
else:
    print("Не палиндром")