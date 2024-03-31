# m = int(input())
# n = int(input())

# if m <= n:
#     for i in range(m, n+1):
#         print(i)
# else:
#     print('error')

# s = 6
# if s == 6:
#     print(s)
# else:
#     print(0)


# Consolas, 'Courier New', monospace


# m = int(input())
# n = int(input())

# if m <= n:
#     for i in range(m, n+1):
#         print(i)
# elif m >= n:
#     for i in range(m, n-1, -1):
#         print(i)


# m = int(input())
# n = int(input())

# if m >= n:
#     for i in range(m, n-1, -1):
#         if i % 2 != 0:
#             print(i)


# m = int(input())
# n = int(input())

# if m <= n:
#     for i in range(m, n+1):
#         if i % 10 == 9:
#             print(i)
#         elif i % 17 == 0:
#             print(i)
#         elif i % 3 == 0 and i % 5 == 0:
#             print(i)
# elif m == n:
#     print(m)


# n = int(input())
#
# for i in range(1, 11):
#     a = n * i
#     print(f'{n} x {i} = {a}')


# from itertools import product
#
# cnt = 0
# for i in product('WORD', repeat = 5):
#     if i.count('R') == 1:
#         cnt += 1
# print(cnt)


a = (2 * 480 * 24 * 512 * 60 * 16) / (2**23 * 25)
print(a)
