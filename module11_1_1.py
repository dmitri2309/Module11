import re

# Ввод данных
data = 'f,f,e,h,e,e,h,h,e,e,f,f,e,e,e,h,e,e,e'
# Разбиваем строку на подстроки по запятым
items = data.split(',')
results = []
i = 0
for item in items:
    if item == "e":
        i += 1
    else:
        results.append(i)
        i = 0
results.append(i)
final_res = [number for number in results if number !=0]
print(final_res)
