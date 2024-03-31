# 4.3

# n = int(input())
# k = int(input())
# if n > k:
#     print('NO')
# elif n < k:
#     print('YES')
# else:
#     print("Don't know")

# a = int(input())
# b = int(input())
# c = int(input())
#
# cnt = 0
#
# if a == b:
#     cnt += 1
# if a == c:
#     cnt += 1
# if b == c:
#     cnt += 1
#
# else:
#     cnt = cnt
#
# if cnt == 3:
#     print('Равносторонний')
# elif cnt == 1:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')


# a = int(input())
# b = int(input())
# c = int(input())
# if b < a < c or c < a < b:
#     print(a)
# elif a < b < c or c < b < a:
#     print(b)
# else:
#     print(c)


# 1, 3, 5, 7, 8, 10, 12 месяцы - 31 день
# 4, 6, 9, 11 - 30
# 2 - 28
# a = int(input())
# if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     print(31)
# elif a == 4 or a == 6 or a == 9 or a == 11:
#     print(30)
# else:
#     print(28)


# a = int(input())
# if a < 60:
#     print('Легкий вес')
# elif 60 <= a < 64:
#     print('Первый полусредний вес')
# elif 64 <= a < 69:
#     print('Полусредний вес')
# else:
#     print('Ошибка')


# a = int(input())
# b = int(input())
# tool = input()
#
# if tool == '+' or tool == '-' or tool == '*' or tool == '/':
#     if tool == '+':
#         print(a + b)
#     if tool == '-':
#         print(a - b)
#     if tool == '*':
#         print(a * b)
#     if tool == '/':
#         if b == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(a / b)
# else:
#     print('Неверная операция')


# a = input()
# b = input()
#
# if (a == 'красный' or a == 'синий' or a == 'желтый') and (b == 'красный' or b == 'синий' or b == 'желтый'):
#     if a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
#         print('фиолетовый')
#     if a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
#         print('оранжевый')
#     if a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
#         print('зеленый')
#     if a == 'красный' and b == 'красный':
#         print('красный')
#     if a == 'синий' and b == 'синий':
#         print('синий')
#     if a == 'желтый' and b == 'желтый':
#         print('желтый')
# else:
#     print('ошибка цвета')


# a = int(input())
#
# if 0 <= a <= 36:
#     if a == 0:
#         print('зеленый')
#     if 1 <= a <= 10:
#         if a % 2 == 0:
#             print('черный')
#         else:
#             print('красный')
#     if 11 <= a <= 18:
#         if a % 2 == 0:
#             print('красный')
#         else:
#             print('черный')
#     if 19 <= a <= 28:
#         if a % 2 == 0:
#             print('черный')
#         else:
#             print('красный')
#     if 29 <= a <= 36:
#         if a % 2 == 0:
#             print('красный')
#         else:
#             print('черный')
# else:
#     print('ошибка ввода')


# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
#
# cnt = 0
#
# if (a1 < b1) and (a2 < b2):
#
#     if b1 == a2:
#         print(b1)
#     elif a1 == b2:
#         print(b2)
#
#     elif (b1 == b2) and (a2 > a1):
#         print(a2, b1)
#     elif a1 == a2:
#         print(a2, b1)
#
#     elif ((b1 < b2) and (b1 > a2)) and (a1 < a2):
#         print(a2, b1)
#     elif (b1 > b2) and (a2 > a1):
#         print(a2, b2)
#
#     elif (b1 > a1) and (b2 > a2) and (a2 > b1):
#         print('пустое множество')
#
#     elif b2 > b1:
#         print(a1, b1)
#     elif (b1 > a1) and (a1 < b2):
#         print(a1, b2)
#
#     elif cnt == 0:
#         print('пустое множество')
# else:
#     print('пустое множество')
