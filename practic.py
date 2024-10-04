# my_numbers = [1,2,3,4,5,6,7,8,9]
#
# result = (x ** 100 for x in my_numbers)
# print(result)
#
# for number in result:
#     print(number)
####################################################
'''Пример того почему генераторную сборку можно выполнить всего один раз'''

# my_numbers = [1,2,3,4,5,6,7,8,9]
#
# result = (x ** 1000 for x in my_numbers)
# for number in result:
#     print(number)
# print("Еще разок")
# for number in my_numbers:
#     print(number)

########################################################
'''Пример того для чего нужна генераторная сборка'''
#
# import time
#
# start_time = time.time()
#
# my_numbers = [1,2,3,4,5,6,7,8,9]
#
# result = (x ** 3000 for x in my_numbers)
# # print(result)
#
# for i in result:
#     print(i)
#
# finish_time = time.time()
# print(f"Время в милисекундах: {(finish_time-start_time)*1000}")

###############################################################

"""Демонстрация ленивых вычеслений с встроенными функциями"""

list_1 = [1,2,3,4,5,6,7]
list_2 = [9,8,7,6,5,54,3,]

ran = range(10, 30)
zp = zip(list_1,list_2)
mp = map(str, list_1)

print(ran,zp,mp)

print(list(ran))
print(list(zp))
print(list(mp))



