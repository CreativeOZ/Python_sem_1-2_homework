# Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды 

second = int(input("Ввести количество секунд: "))
day = second // 86400
second %= 86400
hour = second // 3600
second %= 3600
min = second // 60
second %= 60
print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(day, hour, min, second))