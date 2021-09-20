# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_list = [20, 21, 3, 7, 2, 5, 3, 11, 12]
more_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_list)