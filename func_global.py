x = 50

def func():
    global x

    print('x равен', x)
    x = 2
    print('Заменяем глобальное значение x на', x)

func()
print('Значение х составляет', x)