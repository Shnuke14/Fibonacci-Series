## Запрос количества чисел
count = int(input("Сколько чисел из ряда Фибоначчи вам нужны?")) - 1
## Создание начального ряда
ryad_fiby = [0, 1]
## Задание счётчика
i = 1
## Создание цикла
while i < count:
  ## Добавить в ряд число, равное сумме двух предыдущих
  ryad_fiby.append(ryad_fiby[i] + ryad_fiby[i - 1])
  i += 1

## Вывод ряда Фибоначчи
print(ryad_fiby)