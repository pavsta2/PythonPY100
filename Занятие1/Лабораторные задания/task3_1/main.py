list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
#найти суммуб количество и среднее уникальных чисел

uniqe_numbers = set(list_)
number_uniqe_numbers = len(set(list_))

print(sum(uniqe_numbers))
print(number_uniqe_numbers)
print(sum(uniqe_numbers) / number_uniqe_numbers)

