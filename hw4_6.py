#6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# Например, выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл
def gen1():
    a = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(a), 10): #генерирует 10 чисел начиная с указанного
        print(i)
gen1()

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
def gen2():
    list = [1, 5, None, "this_list"]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(list), 10): #при достижении числа 10 завершаем цикл (повторения)
        print(el)
gen2()