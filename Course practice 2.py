# my_list = [12, None, 53, 'Well i donno what to do', True, 2131.12 ]
#
# for x in my_list:
#     print(type(x))

# elem_count = int(input('Введите количество элементов в списке'))
# my_list = []
# x = 0
# elem = 0
# while x < elem_count:
#     my_list.append(int(input('Какое число добавить в список?')))
#     x = x + 1
#
# for el in range(int(len(my_list))):
#     my_list[elem], my_list[elem + 1] = my_list[elem + 1], my_list[elem]
#     el += 2
# print(my_list)

# my_list = ['Winter', 'Spring', 'Summer', 'Autumn']
# my_dict = {1 : 'Winter', 2 : 'Spring', 3 : 'Summer', 4 : 'Autumn'}
# month = int(input("Введите месяц по номеру "))
# if month ==1 or month == 12 or month == 2:
#         print(my_dict.get(1))
#         # print(my_list[0])
# elif month == 3 or month == 4 or month ==5:
#     print(my_dict.get(2))
#     # print(my_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(my_dict.get(3))
#     # print(my_list[2])
#
# elif month == 9 or month == 10 or month == 11:
#     print(my_dict.get(4))
#     # print(my_list[3])
# else:
#     print("Такого месяца не существует")

# my_list = input("Ваше предложение")
# my_word = []
# num = 1
# for el in range(my_list.count(' ') + 1):
#     my_word = my_list.split()
#     if len(str(my_word)) <= 10:
#         print(f" {num} {my_word [el]}")
#         num += 1
#     else:
#         print(f" {num} {my_word [el] [0:10]}")
#         num += 1


# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг - {my_list}")
# digit = int(input("Введите число"))
# for el in range(len(my_list)):
#     if my_list[el] == digit:
#         my_list.insert(el + 1, digit)
#         break
#     elif my_list[0] < digit:
#         my_list.insert(0, digit)
#     elif my_list[-1] > digit:
#         my_list.append(digit)
#     elif my_list[el] > digit and my_list[el + 1] < digit:
#         my_list.insert(el + 1, digit)
# print(f"Обновленный рейтинг - {my_list}")


# goods = int(input("Какое количество товара хотите внести в базу? "))
# n = 1
# my_dict = []
# my_list = []
# my_analys = {}
# while n <= goods:
#     my_dict = dict({'Название': input("Введите название "), 'Цена': input("Введите цену "),
#                     'Количество': input('Введите количество '), 'Ед': input("Введите единицу измерения ")})
#     my_list.append((n, my_dict))
#     n += 1
#     my_analys = dict(
#         {'Название': my_dict.get('Название'), 'Цена': my_dict.get('Цена'), 'Количество': my_dict.get('Количество'),
#          'Ед': my_dict.get('Ед')})
# print(my_analys)



