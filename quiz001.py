#1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key). keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ожидаемый результат: {1: 1, 2: 4, 3: 9 …} 

def square_dct():
    return {i: i*i for i in range(1, 11)}
print(square_dct())
#2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа. 
def even_list():
    return [2*i for i in range(51)]
print(even_list())
