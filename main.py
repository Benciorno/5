# ЗАДАНИЕ 1

# products_list = []
# class color:
#     BOLD = '\033[1m'
#     END = '\033[0m'
# while True:
#
#         command = input(color.BOLD + "Список комманд:" + color.END + "\n\tadd - Добавить в список продукт."
#                                                                      "\n\tdelete - удалить продукт из списка"
#                                                                      "\n\tshow - показать все имеющиеся продукты"
#                                                                      "\n\tsearch - ищет продукт из списка и выводит его"
#                                                                      "\n\tclear - удаляет все содержимое из списка"
#                                                                      "\n\tstop - останавливает цикл списка" + color.BOLD +
#                         "\nВведите вашу команду:" + color.END).lower()
#         if command == "add":
#             product_name = (input(color.BOLD + "Введите название продукта который вы хотите добавить в список: " + color.END))
#             products_list.append(product_name)
#         elif command == "delete":
#             product_name = (input(color.BOLD + "Введите название продукта который вы хотите удалить из списка: " + color.END))
#             if product_name not in products_list:
#                 print("Данного продукта нету в списке")
#                 continue
#             products_list.remove(product_name)
#         if command == "show":
#             print(products_list)
#         elif command == "search":
#             product_name = (input(color.BOLD + "Введите название продукта который вы хотите найти в списке: " + color.END))
#             if product_name in products_list:
#                 print("Продукт " + color.BOLD + product_name + color.END + " есть в вашем списке")
#             else:
#                 print("Данного продукта нету в списке")
#         elif command == "clear":
#             product_name = (color.BOLD + "Список очищен " + color.END)
#             products_list.clear()
#         elif command == "stop":
#             break

# ЗАДАНИЕ 3

# for i in range(int(input("Введите сколько должно быть ступенек: "))):
#     for num in range(i):
#         print(i, end=" ")
#     print("")

# ЗАДАНИЕ 4

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i % 5 == 0 and i <= 150:
#         print(i)
#     elif i > 500:
#         break

# ЗАДАНИЕ 2

# money = int(input("Какая сумма вашего вклада: "))
# years = int(input("На сколько лет вы вкладываете деньги: "))
# percent = int(input("Какой процент возрастаемости в год: "))
# sum = money * (percent / 100 + 1) ** years
# print("В конце вы получите",sum, "денег")

# ЗАДАНИЕ 5

# num1 = 0
# num2 = 1
# where = int(input("До какого числа: "))
# for numm in range(where):
#     num1, num2 = num2, num1 + num2
#     print(num2, end = " ")
