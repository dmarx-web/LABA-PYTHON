import string

# Ввод строки от пользователя
sequence = input("Введите строку: ").strip()

# Проверяем, что строка не пустая
if not sequence:
    print("Ошибка: введена пустая строка.")
else:
    # Извлекаем знаки препинания и операции отношений
    symbols = set(sequence) & set(string.punctuation + "><=!")
    print("Найденные символы:", symbols if symbols else "Нет знаков препинания или операций отношений")
