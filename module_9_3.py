first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
zp = zip(first, second)
rn = range(len(first) == len(second))

print(list(zp))
print(list(rn))
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) - len(y) != 0)
secnd_result = (len(first[x]) == len(second[x]) for x in range(len(second)))

print(list(first_result))
print(list(secnd_result))


# zp = zip(first_result)
# print(list(zp))