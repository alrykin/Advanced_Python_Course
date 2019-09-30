
# 1)Создать список из N элементов (от 0 до n с шагом 1).
# В этом списке вывести все четные значения.
list_range = []
n = 100
for i in range(n+1):
    list_range.append(i)

for i in list_range:
    if i % 2 == 0:
        print(i)

# 2) СОздать словарь Страна:Столица.
# Создать список стран. Не все страны со списка должны сходиться с названиями стран со словаря.
# С помощою оператора in проверить на вхождение элемента страны в словарь,
# и если такой ключ действительно существует вывести столицу.
country_capitals_dict = {'Ukraine': 'Kyiv', 'Russia': 'Moscow', 'Belarus': 'Minsk'}
country_list = ['Ukraine','USA', 'Belarus']

for i in country_list:
    if i in country_capitals_dict:
        print(country_capitals_dict[i])

# 3) Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
# а вместо чисел, кратных пяти — слово Buzz. Если число кратно пятнадцати,
# то программа должна выводить слово FizzBuzz.
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


# 4) Реализовать функцию bank, которая приннимает следующие аргументы:
# сумма депозита, кол-во лет, и процент.
# Результатом выполнения должна быть сумма по истечению депозита

# в случае выплаты процентов в конце всего срока
def bank(summa_depo, years, percent):
    return(summa_depo+((summa_depo*percent/100)*years))
print(bank(1000,2,10))


# в случае выплаты процентов в конце каждоно года КАПИТАЛИЗАЦИЯ
def bank(summa_depo, years, percent):
    #procents_all = 0
    for i in range(years):
        procent_after_year = summa_depo*percent/100
        summa_depo = summa_depo + procent_after_year
    return(summa_depo)
print(bank(1000,2,10))
