# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

# abc = '"' + 'Python ' + 'is ' + 'a ' + 'great ' + 'language' + '!' + '"' + ', ' + 'said ' + 'Fred' + '. ' \
#       + '"' + 'I ' + "don't " + 'ever ' + 'remember ' + 'having ' + 'this ' + 'much ' + 'fun ' + 'before' + '.' + '"'
# print(abc)


# «Hello [введенное имя] [введенная фамилия]! You have just delved into Python».

# firstname = input()
# surname = input()
# print(f'«Hello {firstname} {surname}! You have just delved into Python.')


# «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

# fc = input()
# line_fc = len(fc)
# print(f'Футбольная команда {fc} имеет длину {line_fc} символов')


# x = (first_digit + second_digit + last_digit) - maxi - mini
# average = (city_1 + city_2 + city_3) - maxi - mini  # average - среднее

# city1 = input()
# city2 = input()
# city3 = input()
# city_1 = len(city1)
# city_2 = len(city2)
# city_3 = len(city3)
#
# maxi = max(city_1, city_2, city_3)
# mini = min(city_1, city_2, city_3)
#
# if maxi == city_1:
#     maxi = city1
# if maxi == city_2:
#     maxi = city2
# if maxi == city_3:
#     maxi = city3
#
# if mini == city_1:
#     mini = city1
# if mini == city_2:
#     mini = city2
# if mini == city_3:
#     mini = city3
#
# print(mini)
# print(maxi)

# a = len(input())
# b = len(input())
# c = len(input())
# # if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
# #     print('YES')
# # else:
# #     print('NO')
# maxi = max(a, b, c)
# mini = min(a, b, c)
# average = (a + b + c) - maxi - mini
# if maxi - average == average - mini:
#     print('YES')
# else:
#     print('NO')


# s = input()
# if 'синий' in s:
#     print('YES')
# else:
#     print('NO')


# s = input()
# if 'суббота' in s or 'воскресенье' in s:
#     print('YES')
# else:
#     print('NO')


# s = input()
# if '@' in s and '.' in s:
#     print('YES')
# else:
#     print('NO')
