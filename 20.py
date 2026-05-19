import random
import time

print("=== ТРЕНАЖЕР ТАБЛИЦЫ УМНОЖЕНИЯ ===")

voprosov = int(input("Сколько примеров?"))
pravilno = 0
oshibki = []
vremena = []

for i in range (voprosov):
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    print(f"\n{i + 1}) {a} * {b} = ?")

    start = time.time()
    otvet = int(input("Ответ: "))
    vremya = time.time() - start
    vremena.append(vremya)

    if otvet == a * b:
        print("Верно!", round(vremya, 1), "сек")
        pravilno += 1
    else:
        print(f"Неверно! Правильно:{a*b}", round(vremya, 1), "сек")
        oshibki.append(f"{a} * {b} = {a*b} (твой ответ: {otvet})")
print("\n" + "="*40)
print("РЕЗУЛЬТАТ:")
print(f"{pravilno}/{voprosov} правильных")
print(f"{pravilno/voprosov*100:.1f}%")
print(f"Среднее время: {sum(vremena)/len(vremena):.2f} сек")

if oshibki:
    print("\nОшибки:")
    for o in oshibki:
        print(" -", o)

if pravilno == voprosov:
    print("\nМолодец! 5+")
elif pravilno >= voprosov*0.7:
    print("\nНеплохо, но можно лучше")
else:
    print("\nУчи таблицу умножения!")

