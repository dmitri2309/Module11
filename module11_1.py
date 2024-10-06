import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# plt.show()                                  # Show the figure.
#

# Работа с модулем pandas. Задача в таблице excel подсчитать количество и вывести в консоль строки которые не содержат значение 'закрыт'
# Чтение данных из файла Excel
filepath = 'Designs.xlsx'
sheet_name = 'Sheet4'
table = pd.read_excel(filepath, sheet_name=sheet_name, header=0)

# Получение индексов строк, где значение в столбце F не равно 'закрыт'
indexes = table[table['Status'] != 'закрыт'].index

# Подсчет количества строк
count = len(indexes)
print("Количество строк:", count)

# Получение значений в столбце A для выбранных строк
values = table.iloc[indexes]['DesID'].tolist()

# Вывод значений в консоль
for value in values:
    print(value)





