a = []
print("Введите ваши значение ")
a1, a2, a3, a4, a5 = map(float, input().split())
l = int(input("На сколько знаков после запятой округлять (я советую 8) "))
cena = float(input("Цену деления введи по-братски "))
a.append(a1)
a.append(a2)
a.append(a3)
a.append(a4)
a.append(a5)
a.sort()
print(a)
R = round(abs(max(a) - min(a)), l)
print("R = ",R)
print(round(abs(a[0] - a[1]),l), " < ", round(0.64 * R, l))
print(round(abs(a[4] - a[3]),l), " < ", round(0.64 * R, l))
if (round(abs(a[0] - a[1]),l) < round(0.64 * R, l) and round(abs(a[4] - a[3]),l) < round(0.64 * R, l)):
    print("Промахов нет")
else:
    print("Промахи есть, удачи!")
znsr = round(sum(a) / 5,l)
print("Среднее значения",znsr)

print("Найдём среднеквадратичное отклонение 𝑆(ско)")
Ssko = round((((a[0] - znsr)**2+(a[1] - znsr)**2+(a[2] - znsr)**2+(a[3] - znsr)**2+(a[4] - znsr)**2)/4)**0.5,l)
print("𝑆(ско) = ",Ssko)
print(round(abs(a[4] - znsr),l), " < ", round(1.67 * Ssko,l))
print(round(abs(a[0] - znsr),l), " < ", round(1.67 * Ssko,l))
if (round(abs(a[4] - znsr),l) < round(1.67 * Ssko,l)) and (round(abs(a[0] - znsr),l) < round(1.67 * Ssko,l)):
    print("Грубых промахов нет!")
else:
    print("Промахи есть, удачи!")
Sskosr = round((Ssko/5**0.5),l)
print("СКО среднего ", Sskosr)
slraz = round((0.51 * R),l)
slsko = round((2.8 * Sskosr),l)
print("Случайная погрешность по размаху ", slraz)
print("Случайная погрешность по СКО ",slsko )
delta = 0
if slraz > slsko:
    delta += slraz
else:
    delta += slsko
polnpog = round((((delta**2) + (cena**2))**0.5),l)
print("Полная погрешность ", polnpog)
print("Относительная погрешность ", round(((polnpog/znsr)*100),l),"%")
print("ИИИИ НАКОНЕЦ")
print("-------------------")
print("ОТВЕТ!")
print(znsr, " ± ", polnpog)