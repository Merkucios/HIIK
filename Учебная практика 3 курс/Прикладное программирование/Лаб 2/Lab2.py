# Задание 1
import pandas as pd
from random import randint
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", 500)

# Задание 2
print("************** Задание 2 ****************")
dictData = {'Хабаровск': 1858, 'Комсомольск-на-Амуре': 1991, 'Владивосток': 1860}

pandaS = pd.Series(data=dictData)
print(pandaS)

# Задание 3 и 4
csvFile = pd.read_csv("data.csv", sep=';')
pandaDF = pd.DataFrame(data=csvFile)
print("************** Задание 3 и 4 ****************")
print(pandaDF)

# Задание 6
print("************** Задание 6 ****************")
pandaDF.loc[len(pandaDF.index)] = ['Zimbabve', 10.3, 5.7, 0.35, 0.45, 4.2, 3.2, 4.9, 10.2, 2.5, ]

new_values = []
for i in range(len(pandaDF.index)):
    new_values.append(randint(4, 40))

pandaDF["Butter"] = new_values
print(pandaDF)

# Задание 7
print("************** Задание 7 ****************")
pandaDF_seven_rows = pandaDF.iloc[9:21]
print(pandaDF_seven_rows)

# Задание 8

dataFrameNewV = pd.DataFrame(
    {
        'Country': ['Angola', 'Belgia', 'Butan', 'Gaiti'],
        'RedMeat': [19, 1.4, 2.5, 13.2],
        'WhiteMeat': [0.4, 15.2, 35.2, 10.2],
        'Eggs': [0.4, 0.2, 0.5, 0.9],
        'Milk': [12.2, 32.1, 3.94, 2.63],
        'Fish': [13.2, 14.5, 13.2, 14.1],
        'Cereals': [29.1, 24.3, 10.2, 14.2],
        'Starch': [4.6, 5.2, 9.2, 13.2],
        'Nuts': [2.5, 9.2, 4.2, 9.4],
        'Fr&Veg': [6.2, 14.2, 9.4, 8.56],
        'Butter': [21.4, 9.2, 23.1, 6.9]
    })
print("************** Задание 8 ****************")
concatTwoDF = pd.concat([pandaDF, dataFrameNewV], ignore_index=True)
print(concatTwoDF)

# Задание 9
print("************** Задание 9 ****************")
new_values = []
for i in range(len(concatTwoDF.index)):
    new_values.append(randint(4, 40))
newAxis = pd.DataFrame(
    {
        'Cucumber': new_values
    }
)

newAxisDF = concatTwoDF.join(newAxis)
print(newAxisDF)

# Задание 10
print("************** Задание 10 ****************")
csvMean = csvFile.mean()
csvStd = csvFile.std()
print(f"********* Среднее значение по файлу: **********\n{csvMean}")
print(f"********* Среднее отклонение по файлу: *********\n{csvStd}")

# Задание 11
print("************** Задание 11 ****************")
csvDescribe = csvFile.describe()
print(f"********* Сводная информация по статистикам: **********\n{csvDescribe}")

# Задание 12
print("************** Задание 12 ****************")
index = newAxisDF.Country
values = newAxisDF.Eggs

plt.bar(index, values)
plt.ylabel('Цена')
plt.title('Ценовая политика яиц', size=14)
plt.xticks(rotation=90, size=7)
plt.show()

newAxisDF.hist()
plt.show()