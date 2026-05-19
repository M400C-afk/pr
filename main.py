import random
import time


def poluchit_chislo(soobschenie, min_zna4enie=None, max_zna4enie=None):
    """Запрашивает у пользователя число, пока не введут правильно"""
    while True:
        try:
            chislo = int(input(soobschenie))
            if min_zna4enie is not None and chislo < min_zna4enie:
                print(f"❌ Число должно быть не меньше {min_zna4enie}! Попробуй снова.")
                continue
            if max_zna4enie is not None and chislo > max_zna4enie:
                print(f"❌ Число должно быть не больше {max_zna4enie}! Попробуй снова.")
                continue
            return chislo
        except ValueError:
            print("❌ Ошибка! Нужно ввести ЦЕЛОЕ число. Попробуй снова.")


def generirovat_primer():
    """Генерирует случайный пример на умножение"""
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    return a, b, a * b


def zadat_vopros(a, b, nomer_voprosa, vsego_voprosov):
    """Задаёт вопрос, получает ответ и замеряет время"""
    print(f"\n📝 Вопрос {nomer_voprosa}/{vsego_voprosov}")
    print(f"{a} x {b} = ?")

    start = time.time()
    otvet = poluchit_chislo("Твой ответ: ")
    vremya = time.time() - start

    return otvet, vremya


proverit_otvet = lambda otvet, pravilniy, vremya: (otvet == pravilniy, vremya)


# ^ лямбда-функция для проверки ответа (возвращает True/False и время)

def obrabotat_otvet(otvet, pravilniy, vremya, pravilno, oshibki):
    """Обрабатывает ответ, обновляет статистику и выводит результат"""
    if otvet == pravilniy:
        print(f"✅ Верно! ({round(vremya, 1)} сек)")
        pravilno += 1
    else:
        print(f"❌ Неверно! Правильно: {pravilniy} ({round(vremya, 1)} сек)")
        oshibki.append(f"{a_global} x {b_global} = {pravilniy} (твой ответ: {otvet})")
        # Используем глобальные переменные для доступа к a и b
    return pravilno


def pokazat_rezultat(pravilno, vsego_voprosov, vremena, oshibki):
    """Показывает итоговую статистику"""
    print("\n" + "=" * 50)
    print("📊 РЕЗУЛЬТАТЫ ТРЕНИРОВКИ 📊")
    print("=" * 50)

    procent = (pravilno / vsego_voprosov) * 100

    print(f"\n✅ Правильных ответов: {pravilno}/{vsego_voprosov}")
    print(f"📈 Процент правильных: {procent:.1f}%")

    if vremena:
        srednee_vremya = sum(vremena) / len(vremena)
        min_vremya = min(vremena)
        max_vremya = max(vremena)
        print(f"\n⏱️ Статистика времени:")
        print(f"   Среднее: {srednee_vremya:.2f} сек")
        print(f"   Самое быстрое: {min_vremya:.2f} сек")
        print(f"   Самое медленное: {max_vremya:.2f} сек")

    if oshibki:
        print(f"\n❌ Ошибки ({len(oshibki)} шт.):")
        for i, oshibka in enumerate(oshibki, 1):
            print(f"   {i}. {oshibka}")
    else:
        print("\n🎉 Поздравляю! НИ ОДНОЙ ОШИБКИ! 🎉")

    print("\n" + "=" * 50)

    # Оценка
    if procent == 100:
        print("🏆 ОТЛИЧНО! Ты знаешь таблицу умножения на 100%! 🏆")
    elif procent >= 90:
        print("🌟 Очень хорошо! Ты почти мастер! 🌟")
    elif procent >= 70:
        print("👍 Хорошо! Но есть над чем поработать! 👍")
    elif procent >= 50:
        print("📚 Неплохо, но нужно больше практики! 📚")
    else:
        print("💪 Тренируйся больше! У тебя всё получится! 💪")

    print("=" * 50 + "\n")


def sprosit_nastroiki():
    """Спрашивает у пользователя настройки тренировки"""
    print("\n⚙️ НАСТРОЙКИ ТРЕНИРОВКИ")
    print("-" * 25)

    voprosov = poluchit_chislo("Сколько примеров решим? (1-50): ", 1, 50)

    print("Диапазон чисел (от 2 до ...)")
    max_chislo = poluchit_chislo("Максимальное число (2-20): ", 2, 20)

    return voprosov, max_chislo


def zapustit_trenazher(voprosov, max_chislo):
    """Основная логика тренажёра"""
    pravilno = 0
    oshibki = []
    vremena = []

    print(f"\n🚀 НАЧИНАЕМ ТРЕНИРОВКУ!")
    print(f"📊 Будет {voprosov} вопросов")
    print(f"🔢 Числа от 2 до {max_chislo}")
    print("-" * 40)

    for i in range(voprosov):
        # Генерируем пример
        a, b, pravilniy_otvet = generirovat_primer()

        # Задаём вопрос
        otvet, vremya = zadat_vopros(a, b, i + 1, voprosov)

        # Сохраняем время
        vremena.append(vremya)

        # Проверяем ответ и обновляем счётчики
        if otvet == pravilniy_otvet:
            print(f"✅ Верно! ({round(vremya, 1)} сек)")
            pravilno += 1
        else:
            print(f"❌ Неверно! Правильно: {pravilniy_otvet} ({round(vremya, 1)} сек)")
            oshibki.append(f"{a} x {b} = {pravilniy_otvet} (твой ответ: {otvet})")

    return pravilno, vremena, oshibki


def sprosit_povtor():
    """Спрашивает, хочет ли пользователь повторить"""
    while True:
        otvet = input("\nХочешь попробовать ещё раз? (да/нет): ").lower()
        if otvet in ['да', 'нет', 'yes', 'no', 'y', 'n', 'д', 'н']:
            return otvet in ['да', 'yes', 'y', 'д']
        else:
            print("❌ Пожалуйста, введите 'да' или 'нет'")


def main():
    """Главная функция программы"""
    print("\n" + "=" * 50)
    print("🎯 ТРЕНАЖЁР ТАБЛИЦЫ УМНОЖЕНИЯ 🎯")
    print("=" * 50)
    print("Добро пожаловать! Я помогу выучить таблицу умножения.")

    while True:
        # Настройка
        voprosov, max_chislo = sprosit_nastroiki()

        # Запуск тренировки
        pravilno, vremena, oshibki = zapustit_trenazher(voprosov, max_chislo)

        # Показ результатов
        pokazat_rezultat(pravilno, voprosov, vremena, oshibki)

        # Спрашиваем о повторе
        if not sprosit_povtor():
            print("\n👋 До свидания! Тренируйся и становись лучше!")
            break


# Запуск программы
if __name__ == "__main__":
    main()