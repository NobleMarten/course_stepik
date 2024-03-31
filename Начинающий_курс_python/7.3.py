# a = int(input())
# b = int(input())
# cnt = 0
# for i in range(a, b+1):
#     if i**3 % 10 == 4 or i**3 % 10 == 9:
#         cnt += 1
# print(cnt)


# n = int(input())
# cnt = 0
# for i in range(n):
#     a = int(input())
#     cnt = cnt + a
# print(cnt)


from math import log

n = int(input())
cnt = 0
for i in range(1, n):
    cnt += 1 / (i + 1)
answer = cnt + 1 - log(n)
print(answer)
