def test_function():

    # Определяем вложенную функцию inner_function

    def inner_function():

        print("Я в области видимости функции test_function")

    # Вызываем inner_function внутри test_function

    inner_function()

# Теперь вызываем test_function, чтобы увидеть результат

test_function()

# Попробуем вызвать inner_function вне test_function

try:

    inner_function()  # Это вызовет ошибку, так как inner_function не доступна вне test_function

except NameError as e:

    print(e)  # Выводим сообщение об ошибке
