numx = int(input("Введите число X: "))

numy = int(input("Введите число Y: "))

if numx > 0 and numy > 0:
   print("Первая четыерть")
elif numx < 0 and numy > 0:
    print("Второая четыерть")
elif numx < 0 and numy < 0:
    print("Третья четыерть")
elif numx > 0 and numy < 0:
    print("Четверть четыерть")