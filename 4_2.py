def test_function():
    def inner_function():
        return 'Я в области видимости функции test_function'

    print(inner_function())
    return


print(test_function())
#print(inner_function())
# Вызывает ошибку, так как в глобальном пространстве ее нет.