def input_set(name):
    while True:
        try:
            # Ввод строки и преобразование в множество целых чисел
            elements = input(f"Введите элементы множества {name} через пробел: ").strip()
            num_set = set(map(int, elements.split()))
            return num_set
        except ValueError:
            print("Ошибка: введите только целые числа, разделенные пробелами.")

# Ввод множеств
A = input_set("A")
B = input_set("B")

# Проверка равенства (A ∪ B) \ B == A
if ((A | B) - B) == A:
    print("Равенство выполняется")
else:
    print("Равенство не выполняется")