# from PIL import Image
# import numpy as np
# import os
# import time
#
# with Image.open("For_Kerzhimanov_not_white_V5.png") as img:
#     img = img.convert("L")
#     print(img.getbands())

data = 'f,f,e,h,e,e,h,h,e,e,f,f,e,e,e,h,e,e,e'

# Разбиваем строку на подстроки по запятым
items = data.split(',')

# Словарь для хранения результатов
results = []
interim_list = []
i = 0
for item in items:
    # Преобразуем строку в число
    try:
        current_item = int(item)
    except ValueError:
        continue

    if current_item == 0:
        interim_list.append(i + 1)
        i = 0
    else:
        i += 1

# Добавляем в результаты количество подряд идущих символов e
if len(interim_list) > 0:
    results.extend([len(lst) for lst in interim_list])

# Формируем итоговый список
final_res = [number for number in results if number != 0]
print(final_res)