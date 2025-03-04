import string

sequence = input("Введите строку: ").strip()

if not sequence:

    print("Ошибка: введена пустая строка.")

else:

    symbols = set(sequence) & set(string.punctuation + "><=!")

    print("Найденные символы:", symbols if symbols else "Нет знаков препинания или операций отношений")
